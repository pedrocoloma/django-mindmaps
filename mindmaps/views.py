from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from .models import Map, Listing
from .forms import UserCreationForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            maps = Map.objects.filter(author=request.user).order_by("-id")
        except Map.DoesNotExist:
            raise Http404("No map found")
        context = {
            "maps": maps,
            "nick": request.user.email.split('@')[0]
        }
        return render(request, 'maps/mymaps.html', context)
    else:
        try:
            listings = Listing.objects.all()
        except Listing.DoesNotExist:
            raise Http404("No listing found")
        context = {
            "maps": Map.objects.all(),
            "listings": listings
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
                    "map": map,
                    "nick": request.user.email.split('@')[0]
                }
            else:
                return render(request, "maps/noaccess.html")

    if request.method == 'POST':  # VERIFICA SE È DO USUÀRIO OU CRIA UM NOVO MAPA
        try:
            map = Map.objects.get(pk=map_id) #public_id=map_id
        except Map.DoesNotExist:
            raise Http404("Map does not exist.")
        if request.user.is_authenticated:
            if map.author == request.user: 
                print("Atualiza o mapa mental")
                mapsjson = request.POST.get('mapsjson')
                mapstitle = request.POST.get('title')
                mapToBeUpdate = Map.objects.get(pk=map_id)
                mapToBeUpdate.mapjson = mapsjson
                mapToBeUpdate.title = mapstitle
                mapToBeUpdate.save()
            else:
                print("Forka o mapa mental")
                title = request.POST.get('title')
                ispublic = False
                author = request.user
                public_id = ""
                friendly_url = ""
                mapjson = request.POST.get('mapsjson')
                language = "pt-br"
                Map.objects.create(title=title, ispublic=ispublic, author=author, public_id=public_id, friendly_url=friendly_url, mapjson=mapjson, language=language)
        else:
            return redirect("login")
        return redirect("index")
    
    return render(request, 'maps/new/index.html', context)

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('index')

def newmindmap(request):
    if request.user.is_authenticated:
        context = {
            "nick": request.user.email.split('@')[0]
        }
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

    if request.user.is_authenticated:
        context = {
            "listings": listings,
            "nick": request.user.email.split('@')[0]
        }
    else:
        context = {
            "listings": listings
        }

    return render(request, "maps/listings.html", context)

def listing(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404("No listing found")
    
    if request.user.is_authenticated:
        context = {
            "listing": listing,
            "maps": listing.maps.all(),
            "nick": request.user.email.split('@')[0]
        }
    else:
        context = {
            "listing": listing,
            "maps": listing.maps.all(),
        }

    return render(request, "maps/listing.html", context)

def myprofile(request):
    context = {}
    return render(request, "profile/myprofile.html", context)

def publicprofile(request, profile_id):
    try:
        maps = Map.objects.filter(author=profile_id, ispublic=True)
    except Map.DoesNotExist:
        raise Http404("Nenhum mapa encontrado")
    # try:
    #     userprofile = CustomUser.objects.get(pk=profile_id)
    # except CustomUser.DoesNotExist:
    #     raise Http404("Nenhum usuário encontrado")
    context = {
        "maps": maps,
        "profile_id": profile_id,
        # "userprofile": userprofile
    }
    return render(request, "profile/publicprofile.html", context)