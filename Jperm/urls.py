from django.conf.urls import patterns, include, url
from Jperm.views import *

urlpatterns = patterns('Jperm.views',
                       url(r'^role/get/$', perm_role_get, name='role_get'),
                       )