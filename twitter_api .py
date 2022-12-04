import tweepy
import configparser
import pandas as pd
import praw

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

# authentication
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

api = tweepy.API(auth)

# Get the latest tweets from the @AuschwitzMuseum account
tweets = api.user_timeline(screen_name="AuschwitzMuseum")

# Print the text and media content of each tweet
for tweet in tweets:
    text = tweet.text
    for media in tweet.entities['media']:
        media_content = media['media_url']




