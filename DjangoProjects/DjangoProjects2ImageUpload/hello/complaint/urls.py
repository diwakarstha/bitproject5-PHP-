from django.contrib import admin
from django.urls import path
from complaint import views

urlpatterns = [
    path("admincomplaint", views.admincomplaint, name='admincomplaint'),
]