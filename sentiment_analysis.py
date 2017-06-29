import tweepy
from textblob import TextBlob

consumer_key = 'aeT8gwsXz84pB4pTtm6VCdQ9i'
consumer_secret = 'uV1NnCovPgIzmuUuF9e3stQs4zpXWXM9fTtffmlHpo1bilp5EF'

access_token = '855475326721208320-91OByoj66cm49ZOACbdGLhAksJklVcd'
access_token_secret = 'rmePpbDkI3KnvGt664QjzszEQqyxmkhsyNHNP6ulSX5kC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('kim kardashian')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

