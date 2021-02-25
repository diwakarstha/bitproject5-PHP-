from django.shortcuts import render, HttpResponse

def admincomplaint(request):
    return render(request, 'useradmin/admincomplaint.html')