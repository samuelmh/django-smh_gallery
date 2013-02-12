from smh_gallery.models import Gallery, Image
from django.contrib import admin

class GalleryAdmin(admin.ModelAdmin):
    fields = ('slug','name','description')
    list_display = ('name', 'slug')

admin.site.register(Gallery, GalleryAdmin)


class ImageAdmin(admin.ModelAdmin):
    fields = ('name','image','description','date','gallery')
    list_display = ('name',)
    list_filter = ('gallery',)

admin.site.register(Image, ImageAdmin)