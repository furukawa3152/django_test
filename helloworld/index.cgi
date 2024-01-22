#!/home/xs146180/hagakurepgm.net/.venv/bin/python
# encoding: utf-8

import sys, os

sys.path.append("/home/xs146180/hagakurepgm.net/public_html/hagakuredjango/")

os.environ['DJANGO_SETTINGS_MODULE'] = "hagakuredjango.settings"

from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)