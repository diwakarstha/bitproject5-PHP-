from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from rooms.models import Room
from enquiry.models import Enquiry
from .models import User
from .forms import EditUserForm, ChangePasswordForm
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages







@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def dashboard(request):
    rooms = Room.objects.filter(user=request.user)
    enquirys = Enquiry.objects.filter()
    context = {
        'enquirys': enquirys,
        'rooms': rooms
    }
    return render(request, 'user/dashboard.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def profile(request):

    users = User.objects.filter(username=request.user)
    context = {
        'users': users
    }
    return render(request, 'user/profile.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def editprofile(request):
    users = User.objects.get(username=request.user)
    form = EditUserForm(instance=users)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'user/editprofile.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def changepassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            messages.error(request, 'Please enter correct passwords.. ')
            return redirect('changepassword')
    else:
        form = ChangePasswordForm(user=request.user)

        args = {'form': form}
        return render(request, 'user/changepassword.html', args)



    # users = User.objects.get(username=request.user)
    # form = ChangePasswordForm()
    # if request.method == 'POST':
    #     form = ChangePasswordForm(request.POST)   
    #     if form.is_valid():
    #         u = User.objects.get(username=request.user)
    #         password = form.cleaned_data['password1']
    #         u.set_password(password)
    #         form.save()
    #         return redirect('profile')
    # context = {
    #     'form': form,
    #     'users': users
    # }

    # return render(request, 'user/changepassword.html',context)
