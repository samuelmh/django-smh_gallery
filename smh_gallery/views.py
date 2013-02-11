
#Django libs
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from smh_gallery.models import Gallery, Image, slugify

#View for a gallery
def gallery_page(request, gallery_name):
    gallery_slug = slugify(gallery_name)
    gallery = get_object_or_404( Gallery, slug=gallery_slug)
    images = Image.objects.filter(gallery=gallery_slug).order_by('-date')
    section = gallery_name
    return (render(request,'gallery.html',locals()))


#View for a gallery item
def image_page(request, gallery_name, image_name):
    gallery = get_object_or_404( Gallery, slug=slugify(gallery_name))  #Check for correct url
    image = get_object_or_404( Image, slug=slugify(image_name))
    section = gallery_name
    return (render(request,'image.html',locals()))