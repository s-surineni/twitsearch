from django.http import HttpResponse

import twitter


twitter_api = twitter.Api(consumer_key='lxsoRrSGKvc8jSVITeLO3ygWb',
                      consumer_secret='LRIjpICLID65jr5kHXPAHNabGnkomvdwLtuNTd6o4tKMmg4koG',
                      access_token_key='54866650-rkf0b9kqKo9l6wCa6YteAFunEMZHwao8asWfcyG74',
                      access_token_secret='GokUcTaleYA5sAzUYo82HEBPyqMqLeoAhcJvhnLcxp63n')


def find_trends(request):
    trends = twitter_api.GetTrendsCurrent()
    print(trends)
    return HttpResponse('hi')
