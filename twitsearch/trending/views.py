import json

from django.http import HttpResponse

from .models import Trend, Tweet

from .search import search_tweets_es, filter_tweets
from .utils import twitter_api, refresh_trends


def find_trends(request):
    refresh_trends()
    return HttpResponse('refreshed trends')


def search_tweets(request):
    request_params = request.GET
    sort_by = None
    if request_params.get('sortBy'):
        sort_by = request_params.get('sortBy')

    if request_params.get('text'):
        text_val = request_params.get('text')
        response = search_tweets_es('tweet_text', text_val, sort_by)
    elif request_params.get('name'):
        name = request_params.get('name')
        response = search_tweets_es('screen_name', name, sort_by)
    elif request_params.get('retweetCount'):
        retweet_count = request_params.get('retweetCount')
        values = request_params.get('values')
        response = filter_tweets('retweet_count', retweet_count, values)
    # print('request.GET', request.GET)
    return HttpResponse(json.dumps(response))
