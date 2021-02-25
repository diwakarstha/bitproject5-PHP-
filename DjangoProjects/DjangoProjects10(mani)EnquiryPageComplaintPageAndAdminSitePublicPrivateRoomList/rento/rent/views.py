from django.shortcuts import render, HttpResponse
from user.decorators import unauthenticated_user, allowed_users

def rent(request):
    return render(request, 'user/rent.html')

