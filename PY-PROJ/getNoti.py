import time
from plyer import notification

if __name__ == "__main__":
    while True:
        # You'll find it better !!
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10
        )
        time.sleep(3600)
