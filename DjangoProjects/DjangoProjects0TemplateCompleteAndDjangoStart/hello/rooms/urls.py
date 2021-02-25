from django.contrib import admin
from django.urls import path
from rooms import views

urlpatterns = [
    path("", views.rooms, name='rooms'),
    path("addroom", views.addroom, name='addroom'),
    path("viewroom", views.viewroom, name='viewroom'),
    path("rooms", views.rooms, name='rooms'),
    path("roomdetail", views.roomdetail, name='roomdetail'),
]  
