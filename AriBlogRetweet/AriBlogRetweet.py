# Importing modules
from time import sleep
import tweepy
import datetime
from decouple import config

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

def get_date_list(tweets):
    # Getting tweet date-time
    date_list1 = []
    for tweet in reversed(tweets):
        created_date = (str(tweet.created_at)).split("+")[0]
        created_date_obj = datetime.datetime.strptime(created_date, '%Y-%m-%d %H:%M:%S')
        date_list1.append(created_date_obj)

    # Getting date-time now    
    data_now = str(datetime.datetime.now())
    data_str = data_now.split(".")
    data_obj = datetime.datetime.strptime(data_str[0], '%Y-%m-%d %H:%M:%S')

    # Getting minute diff of tweet timing and now
    final_minute_list = []
    for i in date_list1:
        result_a = i - data_obj
        result = str((round((result_a.total_seconds())/60)))
        # print(result)
        first_result = result.split(" ")[0]
        final_result = first_result.split("-")[1]
        final_minute_list.append(final_result)
    return final_minute_list

def get_text_list(date_list):
    # Getting tweet text
    text_list1 = []
    for tweet in reversed(tweets):
        if "#myblogs" in tweet.text.lower():
            status = api.get_status(tweet.id, tweet_mode = "extended")
            tweet_text = status.full_text
            text_list1.append(tweet_text)
    new_list = []

    # Checking the time diff is larger or not
    for minute, text in zip(date_list, text_list1):
        if int(minute) > 25000:
            new_list.append(text)
    new_list = list(dict.fromkeys(new_list))
    return new_list

def auto_tweet():
    # Reposting the tweet
    for text in text_list:
        try:
            api.update_status(text)
            print(f"{str(datetime.datetime.now())}  =====  {text}")
        except Exception as e:
            print(f"{str(datetime.datetime.now())}  =====  {e}")

if __name__=='__main__':
    while True:
        tweets = api.user_timeline(screen_name=userID, count=200)
        minute_list = get_date_list(tweets)
        text_list = get_text_list(minute_list)
        print(f"==================================={str(datetime.datetime.now())}===================================\n                                               *****                                                 \n")
        sleep(300)