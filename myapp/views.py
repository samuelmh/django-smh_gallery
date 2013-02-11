
#Django libs
from django.shortcuts import render


def static_section(request, section="home"):
    section = section
    return (render(request, '{section}.html'.format(section=section), locals()))

