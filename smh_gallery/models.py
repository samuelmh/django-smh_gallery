
from django.db import models
from django.template.defaultfilters import slugify

import thumbs


class Gallery(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "galleries"

    def __unicode__(self):
        return(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs) # Call the "real" save() method.


class Image(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name =  models.CharField(max_length=50)
    image = thumbs.ImageWithThumbsField(upload_to='smh_gallery', sizes=((370, 229, thumbs.generate_thumb_max_rectangle),))
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




