
import sys
import time
import config
import telepot
from telepot.loop import MessageLoop


def handle(msg):
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)


token = config.token
bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()
print("Listening")

# Keep the program running
while True:
    time.sleep(10)
