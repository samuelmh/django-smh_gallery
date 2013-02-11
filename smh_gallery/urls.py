

#Django
from django.conf.urls import patterns, url

urlpatterns = patterns('smh_gallery.views',
    url(r'^(?P<gallery_name>[-\w]+)/$', 'gallery_page', name='smh_gallery_gallery'),
    url(r'^(?P<gallery_name>[-\w]+)/(?P<image_name>[-\w]+)/$', 'image_page', name='smh_gallery_image')

)