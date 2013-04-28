#!/usr/bin/python
import os, sys

#If using virtualenv+pip
#import site
#site.addsitedir('web/lib/python2.7/site-packages')

sys.path.append('/web/django-smh_gallery')
sys.path.append('/web')


os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/myapp/trac-eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

