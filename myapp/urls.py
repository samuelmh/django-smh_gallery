

#Django
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'myapp.views.static_section', name='home'),

    # Apps:
    url(r'^gallery/', include('smh_gallery.urls')),

    # Contrib:
    url(r'^admin/', include(admin.site.urls)),

    # If section doesn't matches previous ones, it's static or 404
    url(r'^(?P<section>[-\w]+)/$', 'myapp.views.static_section', name='static_section'),
)
