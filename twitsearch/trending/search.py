from elasticsearch import Elasticsearch

from elasticsearch.helpers import bulk

from elasticsearch_dsl import Date, DocType, Integer, Search, Keyword, Text
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
    user_name = Keyword()
    screen_name = Keyword()
    created_at_in_sec = Integer()
    created_at = Date()
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

text_vals = ['screen_name', 'tweet_text', 'user_name']
int_vals = ['created_at_in_sec', 'favorite_count', 'retweet_count']


def convert_hits_to_dict(response):
    hits_list = []
    for a_hit in response:
        hit_dict = {}
        hit_dict['tweet_text'] = a_hit.tweet_text
        hit_dict['user_name'] = a_hit.user_name
        hit_dict['screen_name'] = a_hit.screen_name
        hit_dict['created_at_in_sec'] = a_hit.created_at_in_sec
        hit_dict['created_at'] = a_hit.created_at
        hit_dict['retweet_count'] = a_hit.retweet_count
        hit_dict['favorite_count'] = a_hit.favorite_count
        hits_list.append(hit_dict)
    return hits_list


def search_tweets_es(key, val, sort_by=None):
    text_vals = ['screen_name', 'tweet_text', 'user_name']
    # int_vals = ['created_at_in_sec', 'favorite_count', 'retweet_count']
    sort_dict = {'sort': {}}
    sort_dict['sort'][sort_by] = {'order': 'asc'}

    if sort_by:
        if sort_by in text_vals:
            sort_dict['sort'][sort_by]['unmapped_type'] = 'text'
        else:
            sort_dict['sort'][sort_by]['unmapped_type'] = 'integer'

    query_dict = {'query': {'match': {key: val}}}
    query_dict.update(sort_dict)

    # q = Q({
    #     "match": {
    #         key: val
    #     }
    # })
    s = Search.from_dict(query_dict)
    print('search dict', s.to_dict())
    response = s.execute()
    response = convert_hits_to_dict(response)
    return response


def filter_tweets(field, value, order):
    if field in int_vals:
        s = Search().filter('range', **{field: {order: value}})
    response = s.execute()
    response = convert_hits_to_dict(response)
    return response


def filter_tweets_by_date(date_range):
    s = Search().filter('range', **{'created_at': {
        "gte": date_range[0],
        "lte": date_range[1]
    }})
    response = s.execute()
    response = convert_hits_to_dict(response)
    return response


def filter_text_fields(text_search):
    if text_search[1] == 'starts with':
        regexpr = text_search[1] + '.*'
    elif text_search[1] == 'ends with':
        regexpr = '.*' + text_search[1]
    else:
        regexpr = '.*' + text_search[1] + '.*'
    query_dict = {
        "query": {
            "regexp": {
               text_search[0]: regexpr
            }
        }
    }
    s = Search.from_dict(query_dict)
    print('search dict', s.to_dict())
    response = s.execute()
    response = convert_hits_to_dict(response)
    return response
