from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    return HttpResponse("ดีจ้า")
