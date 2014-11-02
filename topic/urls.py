from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'topic.views.home', name='home'),
    url(r'^file/upload/$', 'filemanager.views.upload_file', name='upload-topic-file'),
    url(r'^create/$', 'topic.views.create_view', name='create-topic'),
    url(r'^(?P<pk>\d+)/info/$' , 'topic.views.info_view', name='topic-info'),
)
