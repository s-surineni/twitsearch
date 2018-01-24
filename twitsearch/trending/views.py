from django.http import HttpResponse

from .models import Trend

import twitter


twitter_api = twitter.Api(consumer_key='lxsoRrSGKvc8jSVITeLO3ygWb',
                      consumer_secret='LRIjpICLID65jr5kHXPAHNabGnkomvdwLtuNTd6o4tKMmg4koG',
                      access_token_key='54866650-rkf0b9kqKo9l6wCa6YteAFunEMZHwao8asWfcyG74',
                      access_token_secret='GokUcTaleYA5sAzUYo82HEBPyqMqLeoAhcJvhnLcxp63n')


def find_trends(request):
    trends = twitter_api.GetTrendsCurrent()
    for a_trend in trends:
        trend_entity = Trend()
        trend_entity.name = a_trend.name
        trend_entity.url = a_trend.url
        trend_entity.time = a_trend.timestamp
        trend_entity.save()

    print(trends)
    return HttpResponse('hi')
