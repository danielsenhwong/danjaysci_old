from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'danjaysci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # enable admin
    url(r'^admin/', include(admin.site.urls)),

    # admin documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # user authentication
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # my applications
    url(r'^$', include('home.urls')), # home
    url(r'^references/', include('home.urls')), # references
    url(r'^primers/', include('primers.urls', namespace='primers')), # primers
    url(r'^lab_members/', include('lab_members.urls', namespace='lab_members')), #lab_members

)
