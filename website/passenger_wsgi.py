# -*- coding: utf-8 -*-
import os, sys
sys.path.append('/home/d/django17/django17.beget.tech/NurtureVue')
sys.path.append('/home/d/django17/.local/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'NurtureVue.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()