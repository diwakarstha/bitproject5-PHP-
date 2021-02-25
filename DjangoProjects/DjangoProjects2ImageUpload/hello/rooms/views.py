from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .forms import AddRoomForm, EditForm
from .models import City, Location, Room


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
        form = AddRoomForm(request.POST, request.FILES)
        # if request.method == 'POST':
        #     form = AddRoomForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('addroom')
        # return render(request, self.template_name, {'form': form})
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            form = AddRoomForm()
            return redirect('addroom')
        args = {
            'form' : form
        }
        return render(request, self.template_name, args)

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
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'user/viewroom.html',context)

def editroom(request, pk):
    rooms = Room.objects.get(id=pk)
    form = EditForm(instance=rooms)
    context = {
        'form': form,
        'room': rooms
    }
    if request.method == 'POST':
            form = EditForm(request.POST, instance=rooms)
            if form.is_valid():
                form.save()
                return redirect('viewroom')
    return render(request, 'user/editroom.html',context)

def rooms(request):
    return render(request, 'rooms.html')

def roomdetail(request):
    return render(request, 'roomdetail.html')
