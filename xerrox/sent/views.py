from django.shortcuts import render, redirect
from django.conf import settings
from .models import Query, Results
from io import BytesIO
from django.http import HttpResponse


# Create your views here.
import tweepy
import pandas as pd


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

def search(request):
    query = request.GET['query']
    tweets = tweepy.Cursor(api.search_tweets, q=query)
    df = []
    for tweet in tweets.items():
        id = tweet.id
        strid = str(id)
        data = {'tweets':[tweet.text],
                'users':[tweet.user.name],
                'urls' : ['https://twitter.com/twitter/statuses/' + strid]} 
        df.append(pd.DataFrame(data, columns = ['tweets','users','urls']))
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
    




