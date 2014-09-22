from django.conf.urls import patterns, include, url

from plasmids import views

urlpatterns = patterns('',
    # plasmids app urls
    url(r'^$', views.plasmidIndex.as_view(), name='index'), # plasmid index
    url(r'^(?P<pk>\d+)/$', views.plasmidDetail.as_view(), name='detail'), # plasmid detail
    url(r'^(?P<plasmid_id>\d+)/edit/$', views.plasmidEdit, name='edit'), # edit plasmid
    
    url(r'^preps/$', views.prepIndex.as_view(), name='prepIndex'), # dnaPrep index
    url(r'^preps/(?P<pk>\d+)/$', views.prepDetail.as_view(), name='detail'), # dnaPrep detail
    url(r'^(?P<dnaPrep_id>\d+)/edit/$', views.prepEdit, name='edit'), # edit dnaPrep
    
    url(r'^antibiotic/$', views.antibioticIndex.as_view(), name='antibioticIndex'),
    url(r'^antibiotic/(?P<pk>\d+)/$', views.antibioticDetail.as_view(), name='detail'), # dnaPrep detail
    url(r'^(?P<SelectionAntibiotic_id>\d+)/edit/$', views.antibioticEdit, name='edit'), # edit dnaPrep
    
)
