from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'findinggroup.views.home', name='home'),
    url(r'^new/$', 'findinggroup.views.create_new_view'),
    url(r'^my-group/$', 'findinggroup.views.my_group_view'),
)
