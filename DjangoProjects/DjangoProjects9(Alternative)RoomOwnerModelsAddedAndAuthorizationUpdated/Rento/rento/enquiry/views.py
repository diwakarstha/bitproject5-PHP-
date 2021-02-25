from django.shortcuts import render, redirect
from .models import Enquiry
from rooms.models import Room
from enquiry.forms import EnquiryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from user.decorators import allowed_users

@login_required(login_url='user-login')
@allowed_users(allowed_roles='roomowner')
def enquirylist(request):
    enquirys = Enquiry.objects.all()
    return render(request, 'user/enquirylist.html', {'enquirys' : enquirys})

def enquirycreate(request, pk):
    if request.method == 'POST':
        enquiryform = EnquiryForm(request.POST)
        if enquiryform.is_valid():
            data = Enquiry()

            data.room = Room.objects.get(id=pk)
            data.name = enquiryform.cleaned_data['name']
            data.phone = enquiryform.cleaned_data['phone']
            data.email = enquiryform.cleaned_data['email']
            data.address = enquiryform.cleaned_data['address']
            data.occupation = enquiryform.cleaned_data['occupation']
            data.question = enquiryform.cleaned_data['question']
            data.save()
            return redirect('roomdetail', pk)
        return redirect('roomdetail', pk)