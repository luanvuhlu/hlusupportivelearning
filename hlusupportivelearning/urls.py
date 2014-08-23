from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # FONT END:
    url(r'^$', 'hlusupportivelearning.views.home', name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^topic/', include('topic.urls')),
    # BACK END
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^select2/', include('django_select2.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# STATIC
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))