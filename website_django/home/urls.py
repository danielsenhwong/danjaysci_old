from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('home.views',
  url(r'^list/', 'references'), # references/
  url(r'^$', 'index'),  # /
)
