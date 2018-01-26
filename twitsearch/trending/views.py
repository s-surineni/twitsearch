import json

from django.http import HttpResponse

from .models import Trend, Tweet

from.search import match_tweet_text
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
        response = match_tweet_text('tweet_text', text_val, sort_by)
    elif request_params.get('name'):
        name = request_params.get('name')
        response = match_tweet_text('screen_name', name, sort_by)
    # print('request.GET', request.GET)
    return HttpResponse(json.dumps(response))
