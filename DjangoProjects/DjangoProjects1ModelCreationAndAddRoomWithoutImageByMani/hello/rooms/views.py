from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .forms import AddRoomForm
from .models import City, Location


# Create your views here.
class AddRoomView(TemplateView):
    template_name = 'user/addroom.html'

    def get(self, request):
        form = AddRoomForm()
        args = {
            'form': form
            }
        return render(request, self.template_name, args)
    
    def post(self, request):
        # form = AddRoomForm(request.POST)
        # args = {'form': form}
        if request.method == 'POST':
            form = AddRoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addroom')
        return render(request, self.template_name, {'form': form})
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.save()

        #     text = form.cleaned_data
        #     form = AddRoomForm()
        #     return redirect('addroom')
        # text = form.cleaned_data
        # args = {'form': form, 'text': text}
        # return render(request, self.template_name, args)

# AJAX
def load_locations(request):
    city_id = request.GET.get('city_id')
    if city_id == '':
        locations = ""
    else:
        locations = Location.objects.filter(city_id=city_id).all()
    return render(request, 'user/location_dropdown_list_options.html', {'locations': locations})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def viewroom(request):
    return render(request, 'user/viewroom.html')

def rooms(request):
    return render(request, 'rooms.html')

def roomdetail(request):
    return render(request, 'roomdetail.html')
