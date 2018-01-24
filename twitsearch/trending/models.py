from django.db import models


class Trend(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name
