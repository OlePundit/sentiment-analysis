import tweepy
import pandas as pd

api_key = 'SupIZAKQIAOfoZ87Uz9v86Klo'
api_key_secret = 'uPeW9wrShHURXQvVSu7QvEcnAnsbG8pfm6KeHiutn25cAnEn3V'
access_token = '1578435467036561408-E7g83HbrpuIqZjPtUl2M5rsSNp6RWT'
access_token_secret = '9cMoUJUMyoIxh4cLozkWLGtfEjcDm6mc70WxbUPvU17c9'


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search_tweets, q="first community bank")

for tweet in tweets.items():
    data = {'tweets':[tweet.text],
            'users':[tweet.user.name]} 
    df = pd.DataFrame(data, columns = ['tweets','users'])

    df.to_csv('sample12_data.csv', index=False)

    df = pd.read_csv('sample12_data.csv')

    df.to_excel('sample12_data.xlsx', sheet_name='sheet1', index=True)
