from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/index.html')

def bye(request):
    return HttpResponse('<h1>goodbye<h1>')
# Create your views here.
