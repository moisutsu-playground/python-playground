import os
import sys
import traceback
import socket
from datetime import datetime
import functools
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_API_TOKEN = os.environ["SLACK_API_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]


class _Notifier:
    def __init__(self):
        self.api_token = SLACK_API_TOKEN
        self.channel_id = SLACK_CHANNEL_ID
        self.thread_ts = None
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }

    def _post(self, text, to_thread=True):
        try:
            if to_thread:
                self._post_with_thread(text)
            else:
                self._post_without_thread(text)
        except Exception as e:
            print(e, file=sys.stderr)

    def _post_without_thread(self, text):
        requests.post(
            "https://slack.com/api/chat.postMessage",
            headers=self.headers,
            json={
                "channel": self.channel_id,
                "text": text,
            },
        )

    def _post_with_thread(self, text):
        if self.thread_ts is None:
            response = requests.post(
                "https://slack.com/api/chat.postMessage",
                headers=self.headers,
                json={"channel": self.channel_id, "text": text},
            )
            self.thread_ts = response.json()["ts"]
        else:
            requests.post(
                "https://slack.com/api/chat.postMessage",
                headers=self.headers,
                json={
                    "channel": self.channel_id,
                    "text": text,
                    "thread_ts": self.thread_ts,
                },
            )

    def _reset_thread(self):
        self.thread_ts = None

    def _start_function(self, send_message: str):
        self.start_time = datetime.now()
        text = f"function start ✌️\n\n{send_message}"
        self._post(text)

    def _end_function(self, send_message: str):
        elapsed_time = datetime.now() - self.start_time
        text = f"function end :ring:\nTraining duration: {elapsed_time}\n{send_message}"
        self._post(text)
        self._post(text, to_thread=False)

    def send_message(self, text: str, to_thread=True):
        self._post(text, to_thread=to_thread)

    def _error(self, traceback_message: str, send_message: str):
        elapsed_time = datetime.now() - self.start_time
        text = f"Error! ☠️\nCrashed training duration: {elapsed_time}\n{send_message}\nDetail\n{traceback_message}"
        self._post(text)
        self._post(text, to_thread=False)

    @staticmethod
    def _dict2str(info: dict) -> str:
        return "\n".join([f"{key}:\t{value}" for key, value in info.items()])

    @staticmethod
    def _list2str(info: list) -> str:
        return ", ".join([str(elem) for elem in info])

    def decorator(self, start_message=""):
        def inner_decorator(function):
            function_name = function.__name__
            info = {
                "function_name": function_name,
                "machine name": socket.gethostname(),
            }

            @functools.wraps(function)
            def wrapper_function(*args, **kargs):
                self._reset_thread()
                send_message = f"{self._dict2str(info)}\n{self._list2str(args)}\n{self._dict2str(kargs)}"
                self._start_function(f"{start_message}\n{send_message}")  ###
                try:
                    end_message = function(*args, **kargs)
                except Exception as e:
                    self._error(traceback.format_exc(), send_message)
                    raise e
                if end_message is None:
                    self._end_function(send_message)
                else:
                    self._end_function(f"{end_message}\n{send_message}")

            return wrapper_function

        return inner_decorator


SLACK_NOTIFIER = _Notifier()
