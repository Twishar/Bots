
import sys
import asyncio
import telepot
import config
import telepot.aio
from telepot.aio.loop import MessageLoop


def handle(msg):
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)


bot = telepot.aio.Bot(config.token)
loop = asyncio.get_event_loop()


loop.create_task(MessageLoop(bot, handle).run_forever())
print("Listening")

loop.run_forever()
