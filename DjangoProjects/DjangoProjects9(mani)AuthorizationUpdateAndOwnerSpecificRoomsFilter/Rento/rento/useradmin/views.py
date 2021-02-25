from django.shortcuts import render, HttpResponse
from user.decorators import unauthenticated_user, allowed_users


@allowed_users(allowed_roles=['rento_admin'])
def admindashboard(request):
    return render(request, 'useradmin/admindashboard.html')
    
@allowed_users(allowed_roles=['rento_admin'])
def adminchangepassword(request):
    return render(request, 'useradmin/adminchangepassword.html')
