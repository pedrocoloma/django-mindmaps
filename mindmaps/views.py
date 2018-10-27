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
    if request.method == 'GET':
        try:
            map = Map.objects.get(pk=map_id) #public_id=map_id
        except Map.DoesNotExist:
            raise Http404("Map does not exist.")
        if map.ispublic == True:
            if map.mapjson == "":
                map.mapjson = '{"id":"bb41379b-d8df-465f-9361-d816b95ee5ec","title":"Ideia Principal","mindmap":{"root":{"id":"7016f01b-b59a-48f6-9e00-c2471c83be1f","parentId":null,"text":{"caption":"Ideia Principal","font":{"style":"normal","weight":"bold","decoration":"none","size":20,"color":"#000000"}},"offset":{"x":0,"y":0},"foldChildren":false,"branchColor":"#000000","children":[]}},"dates":{"created":1539780082994,"modified":1539780116621},"dimensions":{"x":4000,"y":2000},"autosave":false}'
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

    if request.method == 'POST':
        print("Atualiza o mapa mental")
        mapsjson = request.POST.get('mapsjson')
        mapstitle = request.POST.get('title')
        print(request.POST.get('mapsjson'))
        #Map.objects.get(pk=map_id).update(friendly_url=mapsjson)
        mapToBeUpdate = Map.objects.get(pk=map_id)
        mapToBeUpdate.mapjson = mapsjson
        mapToBeUpdate.title = mapstitle
        mapToBeUpdate.save()
        return redirect("index")
    
    return render(request, 'maps/new/index.html', context)

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
        mapjson = request.POST.get('mapsjson')
        language = "pt-br"
        Map.objects.create(title=title, ispublic=ispublic, author=author, public_id=public_id, friendly_url=friendly_url, mapjson=mapjson, language=language)
        return redirect('index')
    else:
        print("Foi GET")
    context = {}
    return render(request, 'maps/new/index.html', context)

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
