from django.conf.urls import patterns, include, url
from articles import views as articles
from views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UMSK.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teachers$', articles.getTeachers),
    url(r'^$', index, name='home'),
    #url(r'^hello/$', UMSK.hello),
)
