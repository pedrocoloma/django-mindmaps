from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import generic

from .models import Map
from .forms import CustomUserCreationForm

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

class signup(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
