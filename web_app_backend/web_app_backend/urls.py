# web_app_backend/urls.py
from django.urls import path
from .views import get_sensor_data

urlpatterns = [
    path('', get_sensor_data, name='get_sensor_data'),
]





