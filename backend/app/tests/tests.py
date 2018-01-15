"""Tests for the backend"""

from .tools import logprint, AppTestCase, load_file_to_dict

class ExampleScenarioTests(AppTestCase):
    endpoint = 'example_scenario'
    defaults = dict(
        text='',
        files=[]
    )

    def test_backend_call(self):
        """Very simple test where we send a text and a file and check that the
        backend sends back the right response (after some simulated wait)"""
        file_path = ['example_scenario', 'some_data_file.txt']
        files = [load_file_to_dict(file_path)]
        result = self.run_job(job_timeout=60, text='some text', files=files)
        expected_text = 'After deliberation, the answer appears to be 42.'
        self.assertEqual(result['answer_text'], expected_text)
