from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'danjaysci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # enable admin
    url(r'^admin/', include(admin.site.urls)),

    # admin documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # user authentication
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # my applications
    url(r'^$', include('home.urls'), name='home'), # home
    url(r'^', include('home.urls')),
    url(r'^references/', include('home.urls'), name='references'), # references
    url(r'^primers/', include('primers.urls', namespace='primers')), # primers
    url(r'^lab_members/', include('lab_members.urls', namespace='lab_members')), #lab_members
    url(r'^plasmids/', include('plasmids.urls', namespace='plasmids')), # plasmids

)
