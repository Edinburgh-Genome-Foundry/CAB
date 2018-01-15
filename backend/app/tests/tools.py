import os
import base64
import logging
import json
import time
from django.urls import reverse
from django.test import TestCase


def logprint(obj, level='error', prettify=True):
    if prettify:
        if isinstance(obj, dict):
            obj = json.dumps(obj, indent=2)
    level = {
        'error': logging.ERROR
    }[level]
    logging.log(level, str(obj))

test_files_path = os.path.join("app", "tests", "test_files")

def load_file_to_dict(path):
    if isinstance(path, (list, tuple)):
        path = os.path.join(*path)
    full_path = os.path.join(test_files_path, path)
    with open(full_path, 'rb') as f:
        content = base64.b64encode(f.read())
    basename = os.path.basename(full_path)
    _, extension = os.path.splitext(basename)
    mimetype = {
        '.zip': 'application/txt'
    }.get(extension, 'application/txt')
    b64_content = "data:%s;base64,%s" % (mimetype, content.decode('utf8'))
    return {
        'name': basename,
        'content': b64_content
    }


class AppTestCase(TestCase):
    endpoint = 'endpoint'
    defaults = None

    def run_job(self, job_timeout=20, **params):
        # params['synchronous_job'] = True
        defaults = {} if self.defaults is None else self.defaults
        params_with_defaults = {k: v for (k, v) in defaults.items()}
        params_with_defaults.update(params)
        response = self.client.post(reverse(self.endpoint),
                                    json.dumps(params_with_defaults),
                                    content_type='application/json').json()
        if 'job_id' not in response:
            raise IOError("%s" % response)

        job_id = response['job_id']
        t0 = time.time()
        while True:
            time.sleep(0.2)
            elapsed = time.time() - t0
            if elapsed > job_timeout:
                raise IOError("Timeout of job at %s" % self.endpoint)
            response = self.client.post(reverse('poll'),
                                        {'job_id': job_id}).json()
            if response.get('result', False):
                return response['result']
