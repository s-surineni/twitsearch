from datetime import datetime

from django.db import models

from .search import TweetIndex, TrendIndex


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
    created_at = models.DateTimeField(default=datetime.now())
    retweet_count = models.IntegerField()
    favorite_count = models.IntegerField()

    def __str__(self):
        return self.tweet_text

    def indexing(self):
        obj = TweetIndex(
            meta={'id': self.id},
            tweet_text=self.tweet_text,
            user_name=self.user_name,
            screen_name=self.screen_name,
            created_at_in_sec=self.created_at_in_sec,
            created_at=self.created_at,
            retweet_count=self.retweet_count,
            favorite_count=self.favorite_count
        )
        obj.save()
        return obj.to_dict(include_meta=True)
