from django.shortcuts import render
from django.http import HttpResponse

from .models import Map

# Create your views here.
def index(request):
    context = {
        "maps": Map.objects.all()
    }
    return render(request, "maps/index.html")
