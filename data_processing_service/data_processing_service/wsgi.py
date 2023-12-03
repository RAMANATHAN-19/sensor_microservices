from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_processing_service.settings')

application = get_wsgi_application()
