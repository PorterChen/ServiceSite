from django.conf.urls.defaults import *
from django.contrib import admin

from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # (r'^django_multiuploader/', include('django_multiuploader.urls')),
    url(r'^admin/', include('django-log-file-viewer.admin_urls')),

	#(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'', include('multiuploader.urls')),
    url(r'', include('uploadsfiles.urls')),
	url(r'', include('django-log-file-viewer.urls')),
    
) 

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media_site/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 
            settings.MEDIA_ROOT,
            'show_indexes': True}),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
