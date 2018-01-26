from elasticsearch import Elasticsearch

from elasticsearch.helpers import bulk

from elasticsearch_dsl import Date, DocType, Integer, Text, Search
from elasticsearch_dsl.query import Match, Q
from elasticsearch_dsl.connections import connections

from . import models

connections.create_connection()


class TrendIndex(DocType):
    name = Text()
    url = Text()
    time = Date()

    class Meta:
        index = 'trend-index'


class TweetIndex(DocType):
    tweet_text = Text()
    user_name = Text()
    screen_name = Text()
    created_at_in_sec = Integer()
    retweet_count = Integer()
    favorite_count = Integer()

    class Meta:
        index = 'tweet-index'


def bulk_index_trend():
    TrendIndex.init()
    es = Elasticsearch()
    bulk(client=es,
         actions=(b.indexing() for b in models.Trend.objects.all().iterator()))


def bulk_index_tweet():
    TweetIndex.init()
    es = Elasticsearch()
    bulk(client=es,
         actions=(b.indexing() for b in models.Tweet.objects.all().iterator()))


def search(name):
    s = Search().filter('term', name=name)
    response = s.execute()
    return response


def match_tweet_text(text_val):
    q = Q({
        "match": {
            "tweet_text": text_val
        }
    })
    s = Search().query(q)
    response = s.execute()
    hits_list = []
    for a_hit in response:
        hit_dict = {}
        hit_dict['tweet_text'] = a_hit.tweet_text
        hit_dict['user_name'] = a_hit.user_name
        hit_dict['screen_name'] = a_hit.screen_name
        hit_dict['created_at_in_sec'] = a_hit.created_at_in_sec
        hit_dict['retweet_count'] = a_hit.retweet_count
        hit_dict['favorite_count'] = a_hit.favorite_count
        hits_list.append(hit_dict)
    return hits_list
