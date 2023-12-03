# web_app_backend/views.py

from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def get_sensor_data(request):
    # Example logic to fetch data from Data Processing Service
    # This is a placeholder, replace it with your actual logic
    processed_data = {"temperature": 25.5, "motion": "Detected", "humidity": 60.0}
    
    return JsonResponse({"sensor_data": processed_data})

