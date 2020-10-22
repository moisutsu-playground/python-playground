import os
from datetime import datetime
import functools
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_API_TOKEN = os.environ["SLACK_API_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]

class Notifier():
    def __init__(self):
        self.api_token = SLACK_API_TOKEN
        self.channel_id = SLACK_CHANNEL_ID
        self.thread_ts = None
        self.headers = {
            "content-type": "application/json",
            'Authorization': f'Bearer {self.api_token}'
        }

    def _post_with_thread(self, text):
        if self.thread_ts is None:
            response = requests.post("https://slack.com/api/chat.postMessage",
                headers = self.headers,
                json = {
                    "channel": self.channel_id,
                    "text": text
                }
            )
            self.thread_ts = response.json()["ts"]
        else:
            requests.post("https://slack.com/api/chat.postMessage",
                headers = self.headers,
                json = {
                    "channel": self.channel_id,
                    "text": text,
                    "thread_ts": self.thread_ts,
                }
            )

    def _start_function(self, function_name, info: dict):
        names = {
            "file_name": __file__,
            "function_name": function_name,
        }
        self.start_time = datetime.now()
        text = "function start ✌️\n" + "\n".join([f"{key}:\t{value}" for key, value in list(names.items()) + list(info.items())])
        self._post_with_thread(text)

    def _end_function(self):
        elapsed_time = datetime.now() - self.start_time
        text = f"function end :ring:\nTraining duration: {elapsed_time}"
        self._post_with_thread(text)

    def send_message(self, text: str):
        self._post_with_thread(text)

    def _error(self, e):
        text = "Error! ☠️\nDetail\n" + str(e)
        self._post_with_thread(text)

    def decorator(self, **decorator_kargs):
        def inner_decorator(function):
            function_name = function.__name__
            @functools.wraps(function)
            def wrapper_function(*args, **kargs):
                self._start_function(function_name, decorator_kargs)
                try:
                    function(*args, **kargs)
                except Exception as e:
                    self._error(e)
                    raise e
                self._end_function()
            return wrapper_function
        return inner_decorator
