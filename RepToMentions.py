import tweepy
import time
from config import create_api

print('this is my twitter bot', flush=True)


file_name = 'C:\\Users\\krras\\Desktop\\Twitter_Bot\\ast_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open("C:\\Users\\krras\\Desktop\\Twitter_Bot\\last_seen_id.txt", 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open("C:\\Users\\krras\\Desktop\\Twitter_Bot\\last_seen_id.txt", 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    
    last_seen_id = retrieve_last_seen_id(file_name)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, file_name)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)
api=create_api()
while True:
    reply_to_tweets()
    time.sleep(70)