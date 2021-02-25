from django.contrib import admin
from django.urls import path
from feature import views

urlpatterns = [
    path("adminfeature", views.adminfeature, name='adminfeature'),
    path("featureroom", views.featureroom, name='featureroom'),
] 