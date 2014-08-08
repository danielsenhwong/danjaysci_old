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

    # my applications
    url(r'^$', 'danjaysci.views.home', name='home'), # home
    url(r'^primers/', include('primers.urls', namespace='primers')), # primers

)
