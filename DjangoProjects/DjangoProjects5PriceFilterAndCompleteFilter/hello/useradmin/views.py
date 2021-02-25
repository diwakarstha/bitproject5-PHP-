from django.shortcuts import render, HttpResponse

def admindashboard(request):
    return render(request, 'useradmin/admindashboard.html')

def adminchangepassword(request):
    return render(request, 'useradmin/adminchangepassword.html')
