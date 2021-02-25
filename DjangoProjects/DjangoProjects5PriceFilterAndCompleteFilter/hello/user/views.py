from django.shortcuts import render, HttpResponse

def dashboard(request):
    return render(request, 'user/dashboard.html')

def profile(request):
    return render(request, 'user/profile.html')

def editprofile(request):
    return render(request, 'user/editprofile.html')
    
def changepassword(request):
    return render(request, 'user/changepassword.html')
