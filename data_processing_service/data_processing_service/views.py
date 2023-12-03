# data_processing_service/data_processing_service/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def process_data(request):
    processed_data = {"processed_data": "some_processed_data"}
    return JsonResponse(processed_data)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
