from elasticsearch import Elasticsearch

from elasticsearch.helpers import bulk

from elasticsearch_dsl import Date, DocType, Text, Search
from elasticsearch_dsl.connections import connections

from . import models

connections.create_connection()


class TrendIndex(DocType):
    name = Text()
    url = Text()
    time = Date()

    class Meta:
        index = 'trend-index'


def bulk_indexing():
    TrendIndex.init()
    es = Elasticsearch()
    bulk(client=es,
         actions=(b.indexing() for b in models.Trend.objects.all().iterator()))


def search(name):
    s = Search().filter('term', name=name)
    response = s.execute()
    return response
