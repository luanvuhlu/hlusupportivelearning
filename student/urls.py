from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'student.views.home', name='home'),
    url(r'^create/$', 'student.views.create_student_view'),
    url(r'^(?P<code>\w+)/info/$', 'student.views.info_view'),

    # url(r'^account/', include('account.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    # url(r'^select2/', include('django_select2.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
