from re import U
import feedparser
from pprint import pprint
from bs4 import BeautifulSoup
import tweepy
from decouple import config
import logging
import datetime

url = "http://news.google.com/news?q=computational+chemistry&hl=en-US&sort=date&gl=US&num=100&output=rss"

# logging config
logging.basicConfig(level=logging.INFO, filename='data.txt',)
logger = logging.getLogger()


# Keys
CONSUMER_KEY = config('Consumer_Key')
CONSUMER_SECRET_KEY = config('Consumer_Secret_Key')
ACCESS_TOKEN = config('Access_Token')
ACCESS_TOKEN_SECRET = config('Access_Token_Secret')

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
userID = "Aritraroy24Roy"


class ParseFeed():

    def __init__(self, url):
        self.feed_url = url

    def clean(self, html):
        '''
        Get the text from html and do some cleaning
        '''
        soup = BeautifulSoup(html)
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def tweet(self,text_list, url_list):
        try:
            api.update_status(f"#compchem #news #update #science #chemistry #quantum\nTODAY'S UPDATE: {text_list[0]}\n{url_list[0]}")
            print(f"{str(datetime.datetime.now())}  =====  {text_list[0]} === {url_list[0]}")
            logger.info(
                f"Tweet done at : {str(datetime.datetime.now())} === {text_list[0]} === {url_list[0]}\n\n\n")

        except Exception as e:
            print(f"{str(datetime.datetime.now())}  =====  {e}")
            logger.info(
                f"Tweet can't be done at : {str(datetime.datetime.now())} due to {e} error\n\n\n")

    def parse(self):
        '''
        Parse the URL, and print all the details of the news 
        '''
        text_list = []
        url_list = []
        feeds = feedparser.parse(self.feed_url).entries
        for f in feeds:
            text = self.clean(f.get("description"))
            url = f.get("link")
            count = sum((text[i] != ' ') for i in range(len(text)))
            if 100 < count < 200:
                text_list.append(text)
                url_list.append(url)
                # print(f"{count} - {text} - {url}")
        self.tweet(text_list, url_list)


feed = ParseFeed(url)
feed.parse()
