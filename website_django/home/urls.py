from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('home.views',
  url(r'^list/$', 'references', name='list'), # references/
  url(r'^list/(?P<starting_item>[0-9]*)/$', 'references', name='offset'), # references/50
  url(r'^$', 'index'),  # /
)
