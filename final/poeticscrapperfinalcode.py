# import relevant libraries the asynchronous input/output and bot-building python framework
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop

# import relevant libraries to execute the web scraping
from pprint import pprint
from bs4 import BeautifulSoup
import requests

# Telegram bot API token (and its configuration to aysnc version)
TOKEN = '<INSERT API TOKEN HERE>'
bot = telepot.aio.Bot(TOKEN)

# This function will be modified to accommodate our web scraper code afterwards
async def handle(msg):
    # Creating a global variable
    global chat_id
    # These variables will allow us to glance at the received messages - extract the messages' 'headline info'
    content_type, chat_type, chat_id = telepot.glance(msg)
    # Log variables
    print(content_type, chat_type, chat_id)
    # prettify the incoming message
    pprint(msg)

    if content_type == 'text':
        # map the message to the '/start' function
        if msg['text'] == '/start':
            await bot.sendMessage(chat_id, "Hi! I am PoeticScraper and I am able to scrape your desired poem, its credits, the poet's information, and the poem's glossary tags. Key in '/help' for more assistance or any keywords without the '/' to get the ball rolling!")

        # map the message to the '/help' function
        elif msg['text'] == '/help':
            await bot.sendMessage(chat_id, "I am here to help! For starters, you can type any keywords in and I will retrieve the most relevant poem for you! Alternatively, if you have specific poems you want to search, you can do so too! But please note that for poem titles with multiple words, please use '-' between them!")

        # map the message to the '/more' function
        elif msg['text'] == '/more':
            await bot.sendMessage(chat_id, "Can't get enough of poems? Fret not! There are so many other poetry websites for you to browse: www.poetryfoundation.org & www.poets.org.")

        # map the message to the '/video' function
        elif msg['text'] == '/video':
            await bot.sendMessage(chat_id, "To watch the poets perform their poems 'live', please go to https://www.youtube.com/channel/UCQqniBioDz0kgzbDT9ddwKA")

        # map the message to the '/list' function
        elif msg['text'] == '/devices':
            await bot.sendMessage(chat_id, "Everyone can write their own poems! But first, you gotta learn the terms and devices: https://blog.prepscholar.com/poetic-devices-poetry-terms")

        # map the message to the '/data' function
        elif msg['text'] == '/data':
            await bot.sendMessage(chat_id, "I've also created a very basic data visualisation example using a Kaggle dataset and Tableau data visualisation software: https://public.tableau.com/views/Book1_16042958913660/Sheet1?:language=en&:display_count=y&:toolbar=n&:origin=viz_share_link")

        # any other alphabetical input will be under this category (web scraping section)
        elif msg['text'] != '/start' or '/help' or '/more' or '/video' or '/devices' or '/data':
            text = msg['text']
            # it's better to strip and lower the input in order for the subsequent function to comprehend it
            text = text.strip()
            await getInformation(text.lower())

        # if all else fails...
        else:
            await bot.sendMessage(chat_id, "404 not found!")

# the variable 'headers' is required so that the target website perceives our web-scraper as a browser
headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# defining a function - in charge of making the HTTP request, receiving an HTML response, and retrieving the poem
async def getInformation(text):
    # specify the url - all the URLs on this website follow this convention: 'https://poetryarchive.org/poem/<insert poem name>/'
    mainpage_url = 'https://poetryarchive.org/poem/' + text
    # query the website and return the html to the variable 'page'
    page = requests.get(mainpage_url, headers = headers)
    # parse the html using BeautifulSoup and store in variable `soup`
    soup = BeautifulSoup(page.text, 'html.parser')
    pprint(soup)
# this part is crucial to web-scrapping the required information from the webpage
    try:
        # poet's details found by using CSS selector
        try:
            poet = soup.select_one('.poet-name a')['href']
            await bot.sendMessage(chat_id, "This is the poet's details: ")
            await bot.sendMessage(chat_id, poet)
        except:
            await bot.sendMessage(chat_id, "The poet's bio is currently unavailable.")

        # credits/copyright info about the poem
        try:
            credits = soup.find('div', {'class': 'source-box bg-grey pa-boxed small-text'}).text
            await bot.sendMessage(chat_id, "This are the poem's credits: ")
            await bot.sendMessage(chat_id, credits)
        except:
            await bot.sendMessage(chat_id, "No credits found!")

        # textual version of the poem
        try:
            poem = soup.find('div', {'class': 'poem-content'}).text
            await bot.sendMessage(chat_id, "This is the poem: ")
            await bot.sendMessage(chat_id, poem)
        except:
            await bot.sendMessage(chat_id, "Sorry. The poem is currently unavailable.")

        # audio version of the poem found by using CSS selector
        try:
            audio = soup.select_one('.pa-player[audiosrc]')
            message_link = 'Audio link not found'

            if audio:
                message_link = audio['audiosrc']
                await bot.sendMessage(chat_id, "This is the link to access the poem's audio recording: ")
                await bot.sendMessage(chat_id, message_link)
        except:
            await bot.sendMessage(chat_id, "Sorry. The audio recording is currently unavailable.")

        # genre types for this poem
        try:
            meta_tag = soup.select_one('.player-metas a')['href']
            await bot.sendMessage(chat_id, "This is the related glossary tag for this poem: ")
            await bot.sendMessage(chat_id, meta_tag)
        except:
            await bot.sendMessage(chat_id, "Sorry. The glossary tags for this poem are currently unavailable.")
    except:
        await bot.sendMessage(chat_id, "Oh no! Something went wrong... Please enter '/help' for more information.")

# creating the parameters for the bot to run continously and asynchronously
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

# commands the program to keep running forever
loop.run_forever()
