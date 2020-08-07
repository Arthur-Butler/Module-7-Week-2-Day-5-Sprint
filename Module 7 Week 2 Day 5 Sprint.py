#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importin tweepy to access twitter
import tweepy
#importing json to write to ajson file
import json
#importing matplotlib to plot graph
import matplotlib.pyplot
#impotrting tweepy to access twitter
from tweepy import OAuthHandler
#storing keys in public variables
consumer_key = '4lEMOO4PDthOqTXDdbm01RgtI'
consumer_secret = 'ggqfFEZ7nVHFbJgBQKm8TlF3uG58HUfdMwHzn3cEfts0XjiIuC'
access_token = '1267691766028939264-gbsyEyBgkpsRvb56o0jKMVdNfRENbS'
access_secret = 'ADtavjckOMJhd6ZDswaMG6GORYhNwYjcX9qlStKOfy9hm'
#accessing twitter account through api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#getting user input on what to search for
tweet_amount_input= input("Insert number of tweets you want displayed: ")
hashtag = input("What hashtag do you want searched?: ")
tweet_amount=int(tweet_amount_input)
#search input through api
tweets = tweepy.Cursor(api.search,q=hashtag,lang="en",until="").items(tweet_amount)
all_user_data = [[tweet.user.screen_name, tweet.user.location, tweet.user.created_at] for tweet in tweets]
#exporting results to a json folder
with open('twitter.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en",until="").items(tweet_amount):
        f.write(json.dumps(tweet._json)+"\n")
        print("Written to Json file")
#displaying results on graph
tweet_table.plot()
plt.xlabel('Amount of tweets about topic'.format(tweet_amount))
plt.ylabel('Date topic was tweeted about'.format(hashtag))
title('Graph of tweets over time')


# In[ ]:




