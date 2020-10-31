# retrieve basic information about the telegram bot via telepot library
import telepot
# this test-code can only be used if the bot's token is known
bot = telepot.Bot('<INSERT BOT TOKEN HERE>')
bot.getMe()

# see the details of user responses sent to the bot (the type and number of messages sent by who, and the contents of those messages)
from pprint import pprint
response = bot.getUpdates()
pprint(response)

# this is required if we do not want to see the same messages over again (offset will show the newest messsage after this update_id)
bot.getUpdates(offset=<MESSAGE ID>) # update_id + 1 = offset
[]

# test the bot's ability to send messages to the user manually
from telepot.loop import MessageLoop
def handle(msg):
     pprint(msg)

MessageLoop(bot, handle).run_as_thread()
bot.sendMessage(<USER ID>, 'Hey!') # if it works, the user should receive 'Hey!' from the bot on telegram
