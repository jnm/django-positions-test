from django.conf.urls import patterns, include, url
from app.views import silly_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^silly/(?P<photo_id>\d+)$', silly_view),

)
