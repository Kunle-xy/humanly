from django.shortcuts import render
from django.conf.urls.static import static

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')
