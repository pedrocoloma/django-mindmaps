from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:map_id>", views.map, name="map"),
]
