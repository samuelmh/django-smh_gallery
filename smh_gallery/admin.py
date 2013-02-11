from smh_gallery.models import Gallery, Image
from django.contrib import admin

class GalleryAdmin(admin.ModelAdmin):
    fields = ['name','description']
    
admin.site.register(Gallery, GalleryAdmin)


class ImageAdmin(admin.ModelAdmin):
    fields = ['name','image','description','date','gallery']
    list_filter = ['gallery']

admin.site.register(Image, ImageAdmin)