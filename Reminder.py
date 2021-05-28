import time
from plyer import notification  # pip install plyer

while time:
    notification.notify(
        title = "Hello Guys",
        message = "Like, Share and Subscribe",
        app_icon = "C:/Users/Anshu/Desktop/A@YU$H PROJ3CT$/Python/new/Projects/icon.ico",
        timeout=5
    )
    time.sleep(10)