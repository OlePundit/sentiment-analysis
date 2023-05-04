import tweepy
import pandas as pd
import xlsxwriter

api_key = '************'
api_key_secret = '*************************'
access_token = '**********************************'
access_token_secret = '***************************'


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search_tweets, q="first community bank")

df = []
for tweet in tweets.items():
    id = tweet.id
    strid = str(id)
    data = {'tweets':[tweet.text],
            'users':[tweet.user.name],
            'urls':[ 'https://twitter.com/twitter/statuses/' + strid]} 
    df.append(pd.DataFrame(data, columns = ['tweets','users','urls']))
df = pd.concat(df)
df.to_excel('sample13_data.xlsx', sheet_name='sheet1', index=True)

