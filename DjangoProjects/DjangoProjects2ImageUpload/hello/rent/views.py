from django.shortcuts import render, HttpResponse

def rent(request):
    return render(request, 'user/rent.html')

