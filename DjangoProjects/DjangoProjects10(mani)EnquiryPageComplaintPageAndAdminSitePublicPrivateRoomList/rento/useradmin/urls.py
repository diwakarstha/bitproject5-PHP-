from django.contrib import admin
from django.urls import path
from useradmin import views


urlpatterns = [
    path("admindashboard", views.admindashboard, name='admindashboard'),
    path("adminchangepassword", views.adminchangepassword, name='adminchangepassword'),
    path("adminroomlist", views.adminroomlist, name='adminroomlist'),
]