from django.shortcuts import render
from .utils import basemap

def index(request):
    map=basemap(request)
    return render(request, 'geoapp/map.html',  map )
# Create your views here.
