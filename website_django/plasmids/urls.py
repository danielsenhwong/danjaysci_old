from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from plasmids import views

urlpatterns = patterns('',
    # plasmids app urls
    url(r'^$', login_required(views.plasmidIndex.as_view()), name='index'), # plasmid index
    url(r'^(?P<pk>\d+)/$', login_required(views.plasmidDetail.as_view()), name='detail'), # plasmid detail
    url(r'^(?P<plasmid_id>\d+)/edit/$', login_required(views.plasmidEdit), name='edit'), # edit plasmid
    
    url(r'^preps/$', login_required(views.prepIndex.as_view()), name='prepIndex'), # dnaPrep index
    url(r'^preps/(?P<pk>\d+)/$', login_required(views.prepDetail.as_view()), name='prepDetail'), # dnaPrep detail
    url(r'^(?P<dnaPrep_id>\d+)/edit/$', login_required(views.prepEdit), name='prepEdit'), # edit dnaPrep
    
    url(r'^antibiotic/$', login_required(views.antibioticIndex.as_view()), name='antibioticIndex'),
    url(r'^antibiotic/(?P<pk>\d+)/$', login_required(views.antibioticDetail.as_view()), name='antibioticDetail'), # dnaPrep detail
    url(r'^(?P<SelectionAntibiotic_id>\d+)/edit/$', login_required(views.antibioticEdit), name='antibioticEdit'), # edit dnaPrep
    
)
