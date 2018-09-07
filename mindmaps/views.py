from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import Map

# Create your views here.
def index(request):
    context = {
        "maps": Map.objects.all(),
    }
    return render(request, "maps/index.html", context)

def map(request, map_id):
    try:
        map = Map.objects.get(pk=map_id) #public_id=map_id
    except Map.DoesNotExist:
        raise Http404("Map does not exist.")
    context = {
        "map": map
    }
    return render(request, "maps/map.html", context)
