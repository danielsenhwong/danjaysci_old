from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('home.views',
  url(r'^$', 'index'),  # /
  url(r'^', views.references), # references/
)
