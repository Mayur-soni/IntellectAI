"""
WSGI config for ai_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_backend.settings')

# Initialize Django WSGI application first
application = get_wsgi_application()

# Then wrap it with WhiteNoise for static file serving
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'staticfiles'))
