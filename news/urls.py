from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import view_news_detail
urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name='home'),
    url(r'^(?P<pk>\d+)$', view_news_detail, name='view_news_detail'),

)
