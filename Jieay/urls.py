from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('Jieay.views',
    # Examples:
    # url(r'^$', 'mypy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'index', name='index'),
    url(r'^skin_config/$', 'skin_config', name='skin_config'),
    url(r'^login/$', 'Login', name='login'),
    url(r'^logout/$', 'Logout', name='logout'),
    url(r'^Juser/', include('Juser.urls')),
)
