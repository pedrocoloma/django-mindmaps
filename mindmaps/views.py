from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import generic

from .models import Map, Listing
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            maps = Map.objects.filter(author=request.user)
        except Map.DoesNotExist:
            raise Http404("No map found")
        context = {
            "maps": maps
        }
        return render(request, 'maps/mymaps.html', context)
    else:
        context = {
            "maps": Map.objects.all(),
        }
        return render(request, "maps/index.html", context)

def map(request, map_id):
    try:
        map = Map.objects.get(pk=map_id) #public_id=map_id
    except Map.DoesNotExist:
        raise Http404("Map does not exist.")
    if map.ispublic == True:
        context = {
            "map": map
        }
    else:
        if request.user.is_authenticated and map.author == request.user:
            context = {
                "map": map
            }
        else:
            context = {
                "map": {}
            }
    return render(request, "maps/map.html", context)

class signup(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def newmindmap(request):
    if request.user.is_authenticated:
        print("Está autenticado")
    else:
        print("Não está autenticado")

    if request.method == 'POST':
        title=request.POST.get('title')
        ispublic = False
        author = request.user
        public_id = ""
        friendly_url = ""
        language = "pt-br"
        Map.objects.create(title=title, ispublic=ispublic, author=author, public_id=public_id, friendly_url=friendly_url, language=language)
    else:
        print("Foi GET")
    context = {}
    return render(request, 'maps/new.html', context)

def alllistings(request):
    try:
        listings = Listing.objects.all()
    except Listing.DoesNotExist:
        raise Http404("No listing found")
    context = {
        "listings": listings
    }

    return render(request, "maps/listings.html", context)

def listing(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404("No listing found")

    context = {
        "listing": listing,
        "maps": listing.maps.all()
    }

    return render(request, "maps/listing.html", context)
