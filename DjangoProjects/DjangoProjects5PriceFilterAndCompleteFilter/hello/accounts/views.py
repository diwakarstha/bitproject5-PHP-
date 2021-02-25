from django.shortcuts import render

# Create your views here.
def userlogin(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def adminlogin(request):
    return render(request, 'useradmin/adminlogin.html')