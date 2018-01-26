from django.db import models

from .search import TrendIndex


class Trend(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name

    def indexing(self):
        obj = TrendIndex(
            meta={'id': self.id},
            name=self.name,
            url=self.url,
            time=self.time
        )
        obj.save()
        return obj.to_dict(include_meta=True)


class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=50)
    created_at_in_sec = models.IntegerField()
    retweet_count = models.IntegerField()
    favorite_count = models.IntegerField()
