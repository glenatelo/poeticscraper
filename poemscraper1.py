# import relevant files
import requests
from pprint import pprint
from bs4 import BeautifulSoup

# the variable 'headers' is required so that the target website perceives our web-scraper as a browser
headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# defining a function - in charge of making the HTTP request, receiving an HTML response, and retrieving the poem
def getInformation(text):
    # specify the url - all the URLs on this website follow this convention: 'https://poetryarchive.org/poem/<insert poem name>/'
    mainpage_url = 'https://poetryarchive.org/poem/' + text
    # query the website and return the html to the variable 'page'
    page = requests.get(mainpage_url, headers = headers)
    # parse the html using BeautifulSoup and store in variable `soup`
    soup = BeautifulSoup(page.text, 'html.parser')
    pprint(soup)
# this part is crucial to web-scrapping the required information from the webpage
    try:
        # obtain the poet's details
        try:
            poet = soup.find('div', {'class': 'poet-name'}.get('href'))
        except:
            pprint("The poet's details are unavailable at the moment.")
        # credits/copyright info about the poem
        try:
            credits = soup.find('div', {'class': 'source-box bg-grey pa-boxed small-text'}.get('p')).text
        except:
            pprint("No credits found!")
        # audio recording of the poem
        try:
            audio_recording = soup.find('div', {'class': 'pa-player'}.get('audiosrc'))
        except:
            pprint('Sorry. The audio recording is currently unavailable.')
        # textual recording of the poem
        try:
            poem = soup.find('div', {'class': 'poem-content'}).text
        except:
            pprint('Sorry. The poem is currently unavailable.')
    except:
        pprint("Oh no! Something went wrong... You might have to add a '/' at the end of the poem and/or '-' between each word in the poem's name")

# trying to retrieve another poem
word = 'upstream/'
word = word.strip()
getInformation(word)
