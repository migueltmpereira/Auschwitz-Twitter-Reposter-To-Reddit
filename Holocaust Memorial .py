import tweepy
import configparser
import pandas as pd
import praw
import time

# read configs

config = configparser.ConfigParser()
configFilePath = r'/Users/miguempereira/Documents/Projectos/Auschwitz Twitter Reposter to Reddit/config.ini'
config.read(configFilePath)


twitter_api_key = config.get('twitter', 'api_key')
twitter_api_key_secret = config.get('twitter', 'api_key_secret')

twitter_access_token = config.get('twitter', 'access_token')
twitter_access_token_secret = config.get('twitter', 'access_token_secret')

reddit_client_id = config.get('reddit', 'client_id')
reddit_secret_key = config.get('reddit', 'secret_key')
reddit_password = config.get('reddit', 'password')
reddit_username = config.get('reddit', 'username')

# authentication
"""
twitter_auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
twitter_auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitter_api = tweepy.API(auth)
"""
reddit = praw.Reddit(client_id = reddit_client_id,
                     client_secret= reddit_secret_key,
                     password= reddit_password,
                     username= reddit_username,
                     user_agent="Holocaust Memorial by /u/Holocaust_Memorial")

print(reddit.user.me())


# Get the latest tweets from the @AuschwitzMuseum account
#tweets = api.user_timeline(screen_name="AuschwitzMuseum")

# Print the text and media content of each tweet
"""
for tweet in tweets:
    twitter_text = tweet.text
    for media in tweet.entities['media']:
        twitter_media_content = media['media_url'] 
"""

#Subreddit on which I'll post
subreddits =['HolocaustMemorialTest']

#Reddit Post 
#reddit_post_title = twitter_text
#reddit_post_link = twitter_media_content

reddit_post_title = "4 December 1915 | A Pole, Franciszek Masny, was born in Chochołów. A farmer. "
reddit_post_link = "https://pbs.twimg.com/media/FjGvXz0XoAAbq7f?format=jpg&name=900x900"

#Posting on Reddit

count = 0


for subreddit in subreddits:
    try: 
        reddit.subreddit(subreddit).submit(reddit_post_title, url=reddit_post_link)
        print("Successfully posted to ", subreddit, " Posted to ",count,"of ",len(subreddits),"subreddits")
    except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
            #If we are rate limited
            if subexception.error_type == "RATELIMIT":
                #figure out how long to wait before posting again

                wait = str(subexception).replace("RATELIMITE: 'you are doing that too much. try again in ","")
                if 'minute' in wait:
                    wait = wait[:2]
                    wait = int(wait) + 1
                    print(wait)
                else:
                    wait = 1
                
                # Wait for a certain amount of seconds before posting again
                print("waiting for: ",wait," minutes")
                time.sleep(wait*60)
                reddit.subreddit(subreddit).submit(reddit_post_title, url=reddit_post_link)
                print("Successfully posted to ", subreddit, " Posted to ",count,"of ",len(subreddits),"subreddits")



