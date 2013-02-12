
#Django libs
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import Http404

def static_section(request, section="home"):
    section = section
    try:
        return (render(request, '{section}.html'.format(section=section), locals()))
    except TemplateDoesNotExist:
        raise Http404


