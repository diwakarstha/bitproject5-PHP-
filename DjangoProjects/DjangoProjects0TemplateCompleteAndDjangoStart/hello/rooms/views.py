from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def addroom(request):
    return render(request, 'user/addroom.html')

def viewroom(request):
    return render(request, 'user/viewroom.html')

def rooms(request):
    return render(request, 'rooms.html')

def roomdetail(request):
    return render(request, 'roomdetail.html')
