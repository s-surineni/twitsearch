import json

from django.http import HttpResponse

from .models import Trend, Tweet

from .search import *
from .utils import refresh_trends


def find_trends(request):
    refresh_trends()
    return HttpResponse('refreshed trends')


def search_tweets(request):
    request_params = request.GET
    print('request')
    print(request.GET)
    sort_by = None
    response = []
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
    elif request_params.get('date'):
        # print('date: ', request_params.getlist('date'))
        date_range = request_params.getlist('date')
        response = filter_tweets_by_date(date_range)
    elif request_params.get('textSearch'):
        text_search = request_params.getlist('textSearch')
        response = filter_text_fields(text_search)
    # print('request.GET', request.GET)
    return HttpResponse(json.dumps(response))
