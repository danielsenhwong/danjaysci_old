from django.conf.urls import patterns, url

from lab_members import views

urlpatterns = patterns('',
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<lab_member_id>\d+)/edit/$', views.edit, name='edit'),
)
