from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new/', views.newmindmap, name="newmindmap"),
    path("m/<int:map_id>", views.map, name="map"),
    path('u/signup/', views.signup.as_view(), name='signup'),
    path("l/", views.alllistings, name="alllistings"),
    path("l/<int:listing_id>", views.listing, name="listing"),
    path("p/", views.myprofile, name="myprofile"),
    path("p/<int:profile_id>", views.publicprofile, name="publicprofile"),
]
