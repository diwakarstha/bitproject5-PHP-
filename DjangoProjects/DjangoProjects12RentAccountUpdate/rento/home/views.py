from django.shortcuts import render, HttpResponse

# Create your views here.

#visitors page handler
def index(request):
    # context={
    # }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')








