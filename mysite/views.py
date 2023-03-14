from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render

def study(request):
    return render(request, 'study.html')
