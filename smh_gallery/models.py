
from django.db import models
from django.core.files.storage import FileSystemStorage

import thumbs

#Slugified PK
import re
import unidecode



def slugify(str):
    str = unidecode.unidecode(str).lower()
    return re.sub(r'\W+','-',str)


class Gallery(models.Model):
    slug = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "galleries"
    
    
    def __unicode__(self):
        return(self.name)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs) # Call the "real" save() method.

        

fs = FileSystemStorage(location='smh_gallery/static/galleryimages/', base_url="/static/galleryimages/")
class Image(models.Model):
    slug = models.CharField(max_length=200, primary_key=True)
    name =  models.CharField(max_length=200)
    image = thumbs.ImageWithThumbsField(storage=fs, upload_to='./', sizes=((370, 229, thumbs.generate_thumb_max_rectangle),(800,494,thumbs.generate_thumb_max_size)))
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    gallery = models.ForeignKey(Gallery)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return(self.name)
        
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs) # Call the "real" save() method.
    