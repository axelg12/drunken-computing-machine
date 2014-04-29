from django.conf.urls import patterns, include, url
from UMSK.views import * as UMSK
from articles.views import * as articles

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UMSK.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', UMSK.hello),
)
