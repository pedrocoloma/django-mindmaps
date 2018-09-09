from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('m/new/', views.newmindmap, name="newmindmap"),
    path("m/<int:map_id>", views.map, name="map"),
    path('u/signup/', views.signup.as_view(), name='signup'),
]
