# sensor_integration_service/sensor_integration_service/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def sensor_data(request):
    data = request.POST.get('data') 
    return JsonResponse({"status": "success"})
