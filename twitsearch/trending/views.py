from django.http import HttpResponse

from .models import Trend, Tweet

from.search import match_tweet_text
from .utils import twitter_api, refresh_trends


def find_trends(request):
    refresh_trends()
    return HttpResponse('refreshed trends')


def search_tweets(request):
    request_params = request.GET
    if request_params.get('text'):
        text_val = request_params.get('text')
        print('response', match_tweet_text(text_val))
    # print('request.GET', request.GET)
    return HttpResponse('Hello')
