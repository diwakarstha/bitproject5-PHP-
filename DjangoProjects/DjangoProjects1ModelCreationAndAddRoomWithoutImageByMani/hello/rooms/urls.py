from django.contrib import admin
from django.urls import path
from rooms import views
from rooms.views import AddRoomView

urlpatterns = [
    path("", views.rooms, name='rooms'),
    path("addroom", AddRoomView.as_view(), name='addroom'),
    path("viewroom", views.viewroom, name='viewroom'),
    path("rooms", views.rooms, name='rooms'),
    path("roomdetail", views.roomdetail, name='roomdetail'),
    path('ajax/load-locations/', views.load_locations, name='ajax_load_locations'), # AJAX
]  
