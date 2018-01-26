from django.http import HttpResponse

from .models import Trend, Tweet

from .utils import twitter_api, refresh_trends


def find_trends(request):
    refresh_trends()
    return HttpResponse('refreshed trends')
