from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'group.views.home', name='home'),
    url(r'^new/$', 'group.views.save_group_view'),
    url(r'^(?P<id>\d+)/edit/$', 'group.views.save_group_view'),
    url(r'^my-group/$', 'group.views.my_group_view'),
)
