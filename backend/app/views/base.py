import json
import os
import traceback

from rest_framework_tracking.mixins import LoggingMixin

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

import django_rq
import rq
from proglog import RqWorkerBarLogger

class ObjectDict(dict):
    #  TODO: replace by box ?

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        dict.__getattribute__(self, key)

    def __setattr__(self, key, value):
        self[key] = value
        self.__dict__[key] = value

    @staticmethod
    def from_dict(d):
        obj = ObjectDict({
            key: ([
                ObjectDict.from_dict(e)
                if isinstance(e, dict) else e
                for e in value
            ]
                if isinstance(value, (list, tuple))
                else (ObjectDict.from_dict(value)
                      if isinstance(value, dict)
                      else value))
            for (key, value) in d.items()
        })
        for key, value in obj.items():
            sanitized_key = key.replace(" ", "_").replace(".", "_")
            obj.__dict__[sanitized_key] = value
        return obj

    def __repr__(self):
        return "Obj(%s)" % str({
             k: str(v) if (isinstance(v, ObjectDict) or (len(str(v)) < 50))
                       else (str(v)[:50] + "...")
             for k, v in self.items()
        })


class SerializerView(APIView):
    """Base class for a view with a serializer."""
    def serialize(self, request):
        if hasattr(self, 'serializer_class'):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                return ObjectDict.from_dict(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return ObjectDict.from_dict(request.data)


class PollJobView(SerializerView):
    """View returning the status and possibly the result of a job"""
    renderer_classes = (JSONRenderer,)
    class serializer_class(serializers.Serializer):
        job_id = serializers.CharField(label="Job ID")

    def post(self, request, format=None):
        """A view to report the progress to the user."""
        data = self.serialize(request)
        job = django_rq.get_queue("default").fetch_job(data.job_id)
        if job is None:
            return Response(dict(success=False, error="Unknown job ID."))
        job_status = job.get_status()
        success, error = True, ""
        if job_status == "failed":
            success = False
            error = 'There was an uncaught internal error during solving.'
            # print (job.__dict__)
        return Response(
            dict(
                success=success,
                status=job_status,
                error=error,
                progress_data=job.meta.get('progress_data', None),
                result=job.result
            ),
            status=status.HTTP_200_OK
        )

class StartJobView(SerializerView, LoggingMixin):
    renderer_classes = (JSONRenderer, )
    def post(self, request, format=None):
        """ Some description for posts"""
        data = self.serialize(request)
        if not isinstance(data, dict):
            return data
        data["domain_name"] = request.META.get('HTTP_HOST', '')
        job = django_rq.get_queue("default").enqueue(
            self.worker_class.run, data)
        return Response({"job_id": job.id}, status=status.HTTP_200_OK)

class JobResult:

    def __init__(self, json=None, preview_html=None, preview_js=None,
                 file_data=None, file_name=None, file_mimetype=None,
                 error=None):
        self.error = error
        self.json = json
        self.preview_html = preview_html
        self.preview_js = preview_js
        self.file_data = file_data
        self.file_mimetype = file_mimetype
        self.file_name = file_name

    def as_json(self):
        preview = (None if self.preview_html is None else
                   dict(html=self.preview_html, js=self.preview_js))
        file = (None if self.file_data is None else
                dict(data=self.file_data, name=self.file_name,
                     mimetype=self.file_mimetype))
        return dict(error=self.error,
                    json=self.json,
                    preview=preview,
                    file=file)

class AsyncWorker:

    def __init__(self, data, job):

        self.job = job
        self.data = data
        self.logger = RqWorkerBarLogger(job, min_time_interval=100)

    @classmethod
    def run(cls, data):
        job = rq.get_current_job()
        agent = cls(data, job)
        try:
            result = agent.work()
            if isinstance(result, JobResult):
                result = result.as_json()
            return ObjectDict(result)
        except Exception as error:
            trace = traceback.format_exc()
            print (trace)
            return ObjectDict(
                error={'class': error.__class__.__name__,
                       'message': str(error),
                       'trace': trace}
            )
