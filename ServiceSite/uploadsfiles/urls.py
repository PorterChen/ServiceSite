from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'uploadsfiles.views.image_view', name='main'),
)
