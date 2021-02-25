from django.contrib import admin
from django.urls import path
from enquiry import views

urlpatterns = [
    path("enquirylist", views.enquirylist, name='enquirylist'),
]  
