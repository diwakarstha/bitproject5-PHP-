from django.shortcuts import render, redirect
from .models import Enquiry
from rooms.models import Room
from user.models import User
from enquiry.forms import EnquiryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from user.decorators import unauthenticated_user, allowed_users


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def enquirylist(request):
    # rooms = Room.objects.filter(user=request.user)
    enquirys = Enquiry.objects.filter(user=request.user)

    context = {

        'enquirys': enquirys,
        # 'rooms': rooms
    }
    return render(request, 'user/enquirylist.html', context)


def enquirycreate(request, pk):
    if request.method == 'POST':
        enquiryform = EnquiryForm(request.POST)
        if enquiryform.is_valid():
            data = Enquiry()
            user = Room.objects.get(id=pk)
            data.room = Room.objects.get(id=pk)
            data.user = User.objects.get(username=user.user)
            data.name = enquiryform.cleaned_data['name']
            data.phone = enquiryform.cleaned_data['phone']
            data.email = enquiryform.cleaned_data['email']
            data.address = enquiryform.cleaned_data['address']
            data.occupation = enquiryform.cleaned_data['occupation']
            data.question = enquiryform.cleaned_data['question']
            data.save()
            return redirect('roomdetail', pk)
        return redirect('roomdetail', pk)


def roomenqiury(request, pk):
    enquirys = Enquiry.objects.get(id=pk)
    
    context = {
        'enquirys': enquirys
    }
    return render(request, 'user/roomenqiury.html', context)
