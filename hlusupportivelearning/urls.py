from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hlusupportivelearning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^select2/', include('django_select2.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))