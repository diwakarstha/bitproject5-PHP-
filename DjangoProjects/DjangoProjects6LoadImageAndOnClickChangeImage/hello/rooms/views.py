from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .forms import AddRoomForm, EditForm
from .models import City, Location, Room
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    room_list = Room.objects.all()
    locations = Location.get_all_locations()
    locationID = request.GET.get('location')
    facility1 = request.GET.get('water')
    facility2 = request.GET.get('internet')
    facility3 = request.GET.get('parking')
    pricefilter = request.GET.get('pricefilter')
    if not facility1:
        facility1=False
    if not facility2:
        facility2=False
    if not facility3:
        facility3=False
    values = {
            'locationID': locationID,
            'facility1': facility1,
            'facility2': facility2,
            'facility3': facility3,
            'pricefilter': pricefilter,
        }

    #location filter
    if locationID:
        room_list = Room.get_all_rooms_by_filter(locationID)

    #facility filter
    if facility1 or facility2 or facility3:
        room_list = Room.get_all_rooms_by_waterinternetparkingfilter(facility1,facility2,facility3)
    
    if locationID and (facility1 or facility2 or facility3):
        room_list = Room.get_all_rooms_by_allfilter(locationID,facility1,facility2,facility3)
    
    #price filter
    if pricefilter == "1":
        room_list = Room.objects.filter().order_by('price')

    if (pricefilter == "2"):
        room_list = Room.objects.filter().order_by('-price')

    if (pricefilter == "1") and locationID:
        room_list = Room.get_all_rooms_by_filter(locationID).order_by('price')

    if (pricefilter == "2")  and locationID:
        room_list = Room.get_all_rooms_by_filter(locationID).order_by('-price')

    if (pricefilter == "1") and (facility1 or facility2 or facility3):
        room_list = Room.get_all_rooms_by_waterinternetparkingfilter(facility1,facility2,facility3).order_by('price')

    if (pricefilter == "2")  and (facility1 or facility2 or facility3):
        room_list = Room.get_all_rooms_by_waterinternetparkingfilter(facility1,facility2,facility3).order_by('-price')

    if (pricefilter == "1") and locationID and (facility1 or facility2 or facility3):
        room_list = Room.get_all_rooms_by_allfilter(locationID,facility1,facility2,facility3).order_by('price')

    if (pricefilter == "2")  and locationID and (facility1 or facility2 or facility3):
        room_list = Room.get_all_rooms_by_allfilter(locationID,facility1,facility2,facility3).order_by('-price')
        
    #pagination control
    page = request.GET.get('page', 1)

    paginator = Paginator(room_list, 8)
    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)
    
    data = {}
    data['rooms'] = rooms
    data['locations'] = locations
    data['values'] = values
    return render(request, 'rooms.html', data)

def roomdetail(request, pk):
    rooms = Room.objects.get(id=pk)
    if rooms.location:
        print(rooms.location)
        room_list = Room.get_all_rooms_by_filter(rooms.location).exclude(id=pk)
    return render(request, 'roomdetail.html', {'rooms': rooms, 'similarroom': room_list})
