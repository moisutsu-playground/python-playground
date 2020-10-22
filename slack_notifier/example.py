import slack_app
import time

slack_notifier = slack_app.Notifier()

@slack_notifier.decorator(a="Hello")
def sleep_print():
    slack_notifier.send_message("Hello")
    time.sleep(3)
    print("Hello")

if __name__ == "__main__":
    sleep_print()
