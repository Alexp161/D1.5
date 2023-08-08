"""
ASGI configuration for our Django project.

This script exposes the ASGI interface as a module-level variable named `application`.

More information on this file can be found at:
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Setting the default Django settings module for the ASGI application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_asgi_application()
