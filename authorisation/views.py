from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def MyCode(requests):
    try:
        code = requests.GET['code']
        return HttpResponse(code) 
    except:
        return HttpResponse('error')

