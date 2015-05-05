from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    url(r'^twilio/', include('twilio_app.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
