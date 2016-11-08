from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check/(?P<team1>[\w\s]+)/(?P<team2>[\w\s]+)/$', views.check, name='check'),
]