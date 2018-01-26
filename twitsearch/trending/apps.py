from django.apps import AppConfig


class TrendingConfig(AppConfig):
    name = 'trending'

    def ready(self):
        import trending.signals
