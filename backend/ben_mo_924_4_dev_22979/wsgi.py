"""
WSGI config for ben_mo_924_4_dev_22979 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ben_mo_924_4_dev_22979.settings')

application = get_wsgi_application()
