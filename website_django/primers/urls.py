from django.conf.urls import patterns, url

from primers import views

urlpatterns = patterns('',
  # /primers/
  url(r'^$', views.IndexView.as_view(), name='index'),
  # /primers/1/
  url(r'^(?P<primer_id>\d+)/$', views.DetailView.as_view(), name='detail'),
  # /primers/1/edit/
  url(r'^(?P<primer_id>\d+)/edit/$', views.edit, name='edit'),
)
