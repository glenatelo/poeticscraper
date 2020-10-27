# poeticscrapper
All the resources used for the 'PoeticScrapper' Telegram bot.

The code(s) included in this repository:
a) telegramtestbed.py - this piece of code is mainly used to test the functionality of the bot (when it is newly created by BotFather), such as sending/receiving messages from specific users. This code need not be used anymore once the bot's functionality is verified.

b) bot1.py - this piece of code is important to handle the user requests in terms of retrieving the required information from the website, i.e. establishing the asynchronous input/output characteristics of the bot, the type of reply to be sent to the user, and how long the bot will run for.

c) poemscraper1.py - this piece of code is the 'heart of the telegram bot' as it contains the main functions required for the web-scraping to be executed by the telegram bot.

d)

So, how do these codes come together to form the bot? These are the steps:
1) Create a brand-new bot via telegram's BotFather master bot (https://t.me/botfather).
