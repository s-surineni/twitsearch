import twitter

from .models import Trend, Tweet
from datetime import datetime

# twitter_api = twitter.Api(consumer_key='lxsoRrSGKvc8jSVITeLO3ygWb',
#                           consumer_secret='LRIjpICLID65jr5kHXPAHNabGnkomvdwLtuNTd6o4tKMmg4koG',
#                           access_token_key='54866650-rkf0b9kqKo9l6wCa6YteAFunEMZHwao8asWfcyG74',
#                           access_token_secret='GokUcTaleYA5sAzUYo82HEBPyqMqLeoAhcJvhnLcxp63n')


twitter_api = twitter.Api(consumer_key='JZUpKuBpeoXG05mhCMmSt3slc',
                          consumer_secret='QadwBZKMAuW79ktICL5KHodMC5CXPdC3NX1ZT7zvgsHTE9W3mW',
                          access_token_key='956820967635890176-vvxIixfNPITXZeKFeARZwjB1bYl4wC0',
                          access_token_secret='xqlGSbMvAVXQTJ4PhbrNsAc6X2qsthBChxrPFZ2lbx8mz')

def refresh_trends():
    trends = twitter_api.GetTrendsCurrent()
    for a_trend in trends:
        print('Fetching trends for trend %s' % (a_trend.name))
        a_trend.name = a_trend.name.split('#')[1] if '#' in a_trend.name else a_trend.name
        query = "q=%23{0}&result_type=recent&count=5&include_entities=true".format(a_trend.name)
        trend_tweets = twitter_api.GetSearch(raw_query=query)
        for a_trnd_twt in trend_tweets:
            tweet_entity = Tweet()
            tweet_entity.tweet_text = a_trnd_twt.text
            tweet_entity.user_name = a_trnd_twt.user.name
            tweet_entity.screen_name = a_trnd_twt.user.screen_name
            tweet_entity.created_at_in_sec = a_trnd_twt.created_at_in_seconds
            tweet_entity.created_at = datetime.fromtimestamp(a_trnd_twt.created_at_in_seconds)
            tweet_entity.retweet_count = a_trnd_twt.retweet_count
            tweet_entity.favorite_count = a_trnd_twt.favorite_count
            tweet_entity.save()
        trend_entity = Trend()
        trend_entity.name = a_trend.name
        trend_entity.url = a_trend.url
        trend_entity.time = a_trend.timestamp
        trend_entity.save()
        break
