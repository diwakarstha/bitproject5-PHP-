from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import User
from user.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, 'login.html')

@login_required(login_url='user-login')
def logoutuser(request):
    logout(request)
    return redirect('user-login')

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user-login')
        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)

def adminlogin(request):
    return render(request, 'useradmin/adminlogin.html')