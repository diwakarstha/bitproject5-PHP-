from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def dashboard(request):
    return render(request, 'user/dashboard.html')

@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

@login_required(login_url='user-login')
def editprofile(request):
    return render(request, 'user/editprofile.html')

@login_required(login_url='user-login')
def changepassword(request):
    return render(request, 'user/changepassword.html')
