"""
WSGI config for quali project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

project_home = u'/var/www/qualihewa.com/public_html/qualihewa'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quali.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
