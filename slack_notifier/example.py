from slack_app import SLACK_NOTIFIER
import time


@SLACK_NOTIFIER.decorator()
def sleep_print(a, b, c, d):
    SLACK_NOTIFIER.send_message("Hello")
    time.sleep(3)
    SLACK_NOTIFIER.send_message("World")
    return "Finish"


@SLACK_NOTIFIER.decorator("start message", notify_stop=True)
def use_all_method(a, b):
    SLACK_NOTIFIER.send_message("to thread")
    SLACK_NOTIFIER.send_message("send message", to_thread=False)
    return "end message"


@SLACK_NOTIFIER.decorator()
def raise_error():
    [][0]


if __name__ == "__main__":
    sleep_print(3, 2, c="Hello", d="World")
    use_all_method(10, b=10)
    raise_error()
