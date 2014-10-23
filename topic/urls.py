from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'topic.views.home', name='home'),
    url(r'^create/$', 'topic.views.create_view', name='create-topic'),

)
