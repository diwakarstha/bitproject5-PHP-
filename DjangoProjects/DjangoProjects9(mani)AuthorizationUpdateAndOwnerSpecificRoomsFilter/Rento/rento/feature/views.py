from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated_user, allowed_users

# Create your views here.
@allowed_users(allowed_roles=['rento_user'])
def featureroom(request):
    return render(request, 'user/featureroom.html')
@allowed_users(allowed_roles=['rento_admin'])
def adminfeature(request):
    return render(request, 'useradmin/adminfeature.html')