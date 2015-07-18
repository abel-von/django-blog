from django.conf.urls import patterns, include, url

from django.contrib import admin
import myblog
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',  include('blog.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   url(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': myblog.settings.MEDIA_ROOT },name="media")
    
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()