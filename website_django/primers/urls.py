from django.conf.urls import patterns, url

from primers import views

urlpatterns = patterns('',
  # /primers/
  url(r'^$', views.index, name='index'),
  # /primers/1/
  url(r'^(?P<primer_id>\d+)/$', views.detail, name='detail'),
)
