from django.contrib import admin
from django.urls import path
from rent import views

urlpatterns = [
    path("rent", views.rent, name='rent'),
]