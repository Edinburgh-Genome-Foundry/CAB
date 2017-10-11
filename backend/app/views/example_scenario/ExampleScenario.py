"""Bla."""

from ..base import AsyncWorker, StartJobView, JobResult
from ..serializers import FileSerializer
from rest_framework import serializers
import time

# Every component of the frontend form must have its serializer.

class serializer_class(serializers.Serializer):
    text = serializers.CharField()
    files = serializers.ListField(child=FileSerializer())


class worker_class(AsyncWorker):

    def work(self):

        self.logger(message="This message will be shown to the website user!")

        # You can access any data from the frontend form as follows:

        user_text = self.data.text
        user_files = self.data.files

       # ====================================================================
       #
       # Here you would write some code to process the user's input using
       # your awesome libraries to produce magnificent results.
       #
       # ====================================================================

        for i in self.logger.iter_bar(loop=range(6)):
            if i == 3:
                self.logger(message="Hey we're halfway through!")
            for j in self.logger.iter_bar(subloop=range(50)):
                time.sleep(0.1)

        # When the computations are done, return some results data.
        # The data returned will be displayed by the frontend app in the
        # results section

        return {
          'answer_text': 'After deliberation, the answer appears to be 42.',
          'figures_data': '(yep, you can send back figure data, see the other'
                          'app for examples)'
        }

class ExampleScenarioView(StartJobView):
    '''This will be the same for every scenario you write.'''
    serializer_class = serializer_class
    worker_class = worker_class
