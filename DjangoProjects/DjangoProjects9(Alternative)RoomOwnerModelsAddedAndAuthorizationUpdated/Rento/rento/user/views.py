from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user.decorators import allowed_users

@login_required(login_url='user-login')
@allowed_users(allowed_roles='roomowner')
def dashboard(request):
    return render(request, 'user/dashboard.html')

@login_required(login_url='user-login')
@allowed_users(allowed_roles='roomowner')
def profile(request):
    return render(request, 'user/profile.html')

@login_required(login_url='user-login')
@allowed_users(allowed_roles='roomowner')
def editprofile(request):
    return render(request, 'user/editprofile.html')

@login_required(login_url='user-login')
@allowed_users(allowed_roles='roomowner')
def changepassword(request):
    return render(request, 'user/changepassword.html')
