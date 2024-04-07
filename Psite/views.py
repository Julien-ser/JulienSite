from django.shortcuts import render, redirect
from django.http import JsonResponse
from Psite import backend
from django.views.decorators.csrf import csrf_exempt
#from .models import Prompt
import asyncio
import test
import requests
import time

# Create your views here.
def index(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        print(prompt1)
        result = backend.getResp(prompt1)[0]["generated_text"]
        print(result)
        response_data = {
            'result': result, 
        }
        return JsonResponse(response_data)
    else:
        return render(request, 'index.html')