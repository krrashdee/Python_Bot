import tweepy
import logging
from config import create_api
import time
api=create_api()
print("Liking Home timeline")
while True:

	tweets_home=api.home_timeline(count=10)
	for tweet in tweets_home:
		if not tweet.favorited:
			print(f"Liking {tweet.id} ({tweet.author.name})")
			api.create_favorite(tweet.id)
	time.sleep(100)
