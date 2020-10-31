# poeticscrapper
All the resources used for the 'PoeticScrapper' Telegram bot. Please note that I used a laptop running Windows10 and I created, edited, and ran the subsequent codes via Atom (after I installed additional packages on it).

The code(s) included in this repository:

a) telegramtestbed.py - this piece of code is mainly used to test the functionality of the bot (when it is newly created by BotFather), such as sending/receiving messages from specific users. This code need not be used anymore once the bot's functionality is verified.

b) asynciobot.py - this piece of code is important to handle the user requests in terms of retrieving the required information from the website, i.e. establishing the asynchronous input/output characteristics of the bot, the type of replies to be sent to the user, and how long the bot will run for.

c) webscraper.py - this piece of code is the 'heart of the telegram bot' as it contains the main functions required for the web-scraping to be executed by the telegram bot.

d) telebotfinal.py - this piece of code is the final product that houses all the lines of code required to run the telegram bot locally. It possesses functions that are defined to (i) map keywords to specific actions and (ii) specify the elements on the webpage that will be scraped by the bot. All of these are enabled by the aforementioned bot1.py code (that has been inserted into this piece of code).

DISCLAIMER: The bot can be accessed by searching @PoeticScraper_bot on Telegram. However, do note that it can only run locally (on my laptop terminal) as of right now.


**Note that scrapefm1.py (in 'initial football manager idea' folder) is the piece of code that I created for my initial project idea (SCRAPPED), and it does not have any bearing on the current Poetic Scraper bot.** 
