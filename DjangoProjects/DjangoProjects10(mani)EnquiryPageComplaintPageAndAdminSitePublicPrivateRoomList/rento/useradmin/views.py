from django.shortcuts import render, HttpResponse
from user.decorators import unauthenticated_user, allowed_users
from rooms.models import Room
from user.models import User


@allowed_users(allowed_roles=['rento_admin'])
def admindashboard(request):
      
    rooms = Room.objects.all()
    users = User.objects.all()
    content = {
        'users':users,
        'rooms':rooms
    }

    return render(request, 'useradmin/admindashboard.html',content)
    
@allowed_users(allowed_roles=['rento_admin'])
def adminchangepassword(request):
    return render(request, 'useradmin/adminchangepassword.html')


@allowed_users(allowed_roles=['rento_admin'])
def adminroomlist(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, 'useradmin/adminroomlist.html',context)
