from django.shortcuts import render

# Create your views here.
def featureroom(request):
    return render(request, 'user/featureroom.html')

def adminfeature(request):
    return render(request, 'useradmin/adminfeature.html')