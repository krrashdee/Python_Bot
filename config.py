# QUERY="# python"
# LIKE=True
# FOLLOW=True
# SLEEP_TIME=300
import credentials
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = credentials.consumer_key
    consumer_secret = credentials.consumer_secret
    access_token = credentials.access_token
    access_token_secret = credentials.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api