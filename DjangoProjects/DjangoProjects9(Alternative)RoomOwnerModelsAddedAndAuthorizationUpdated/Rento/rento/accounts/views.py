from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import RoomOwner
from user.decorators import unauthenticated_user
from user.forms import CreateUserForm, RoomOwnerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def userlogin(request):
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

@unauthenticated_user
def registration(request):
    form = CreateUserForm()
    profile_form = RoomOwnerForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = RoomOwnerForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            group = Group.objects.get(name='roomowner')
            user.groups.add(group)
            return redirect('user-login')
    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'registration.html', context)

def adminlogin(request):
    return render(request, 'useradmin/adminlogin.html')