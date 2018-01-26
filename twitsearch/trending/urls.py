from django.urls import path

from . import views

urlpatterns = [
    path('find_trends', views.find_trends),
    path('search_tweets', views.search_tweets),
]
