from django.shortcuts import render, HttpResponse

# Create your views here.

#visitors page handler
def index(request):
    # context={
    # }
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("this is contactpage")








