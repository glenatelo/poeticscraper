# import relevant libraries
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop

# This function will be modified to accommodate our web scraper code afterwards
async def handle(msg):
    # These variables will allow us to glance at the received messages - extract the messages' 'headline info'
    content_type, chat_type, chat_id = telepot.glance(msg)
    # Log variables
    print(content_type, chat_type, chat_id)
    pprint(msg)
    # Send our JSON msg variable as reply message
    await bot.sendMessage(chat_id, msg)

# creating the parameters for the bot to run continously and asynchronously
TOKEN = '<INSERT TOKEN HERE>'
bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

# commands the program to keep running forever
loop.run_forever()
