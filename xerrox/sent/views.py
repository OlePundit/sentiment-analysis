from django.shortcuts import render, redirect
from django.conf import settings
from .models import Query, Results
from io import BytesIO
from django.http import HttpResponse
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Create your views here.
import tweepy
import pandas as pd
import xlsxwriter


authenticator = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
authenticator.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

def index(request):
    if request.method == 'POST':
        query=request.POST.get('query')
        en= Results(query=query)
        en.save()
        return redirect('search')
    
    return render(request, 'index.html',)


def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
   
    print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
 
    else :
        print("Neutral")    

def search(request):
    analyzer = SentimentIntensityAnalyzer()
    query = request.GET['query']
    tweets = tweepy.Cursor(api.search_tweets, q=query)
    df = []
    for tweet in tweets.items():
        id = tweet.id
        strid = str(id)
        sentence = tweet.text 
        sentimentality = (analyzer.polarity_scores(sentence)["compound"])
        
        
        if sentimentality >= 0.05:
            sentimentality = 'Positive'
        elif sentimentality <= -0.05:
            sentimentality  = 'Negative'
        else :
            sentimentality = 'Neutral'

        data = {'tweets':[tweet.text],
                'users':[tweet.user.name],                
                'urls' : ['https://twitter.com/twitter/statuses/' + strid],
                'sentiment': [sentimentality]}
             
        df.append(pd.DataFrame(data, columns = ['tweets','users','urls','sentiment']))
    df = pd.concat(df)

    
    #engine=create_engine('sqlite:///db.sqlite3')
    #df.to_sql(Query._meta.db_table, if_exists='replace', con=engine, index=False)
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        # Set up the Http response.
        filename = 'sentiment-analysis.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


    





