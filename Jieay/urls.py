from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('Jieay.views',
    # Examples:
    # url(r'^$', 'Jieay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'Login', name='login'),
    url(r'^logout/$', 'Logout', name='logout'),
)
