from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def enquirylist(request):
    return render(request, 'user/enquirylist.html')