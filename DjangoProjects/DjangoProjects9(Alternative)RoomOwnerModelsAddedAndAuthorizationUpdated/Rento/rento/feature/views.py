from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user-login')
def featureroom(request):
    return render(request, 'user/featureroom.html')

def adminfeature(request):
    return render(request, 'useradmin/adminfeature.html')