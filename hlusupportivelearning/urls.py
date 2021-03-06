from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from filebrowser.sites import site
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
import settings
from views import search_full
admin.autodiscover()

urlpatterns = patterns('',
    # FONT END:
    url(r'^$', 'hlusupportivelearning.views.home', name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^topic/', include('topic.urls')),
    url(r'^group/', include('group.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^tag/', include('tag.urls')),
    url(r'^document/', include('document.urls')),
    url(r'^date/', include('datemanager.urls')),
    url(r'^letgo/', 'hlusupportivelearning.views.getting_started', name='getting_started'),
    url(r'^search/', search_full),
    # BACK END
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^select2/', include('django_select2.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
)

# STATIC
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
# MEDIA
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))
# Debug ToolBar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )