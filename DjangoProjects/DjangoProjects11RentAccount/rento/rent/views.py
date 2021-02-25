from django.shortcuts import render, HttpResponse, redirect
from user.decorators import unauthenticated_user, allowed_users
from .models import DateTracker, Rent
from user.models import User
from rooms.models import Room
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['rento_user'])
def rent(request):
    rooms = Room.objects.filter(user=request.user)
    check_rent = Rent.objects.filter(user=request.user)
    database_date = DateTracker.objects.get(user=request.user)
    if not check_rent:
        datetracker = DateTracker()
        datetracker.user = User.objects.get(username=request.user)
        datetracker.date_updated = datetime.now().date()
        datetracker.save()
    else:
        datetracker = DateTracker.objects.get(user=request.user)
        datetracker.date_updated = datetime.now().date()
        datetracker.save()
    for room in rooms:
        print(room.pk)
        if not check_rent:
            data = Rent()
            data.user = User.objects.get(username=request.user)
            data.room_tag = room.pk
            data.amount = room.price
            data.amount_paid = 0
            data.due = room.price
            data.advance = 0
            data.rent_status = "due"
            data.save()
        else:
            date_difference = ((datetime.now().date().year - database_date.date_updated.year)
                               * 12+datetime.now().date().month-database_date.date_updated.month)
            if date_difference > 0:
                print(str(date_difference)+" success "+str(room.price))
            # print(datetime.now().date()- datetime(2021,1,10).date() - database_date.date_updated.year)
                rent_detail = Rent.objects.get(room_tag=room.pk)
                updated_due = rent_detail.due + date_difference*room.price - rent_detail.advance
                if updated_due < 0:
                    updated_advance = abs(updated_due)
                    updated_due = 0
                    rent_detail.rent_status = "advance"
                elif updated_due == 0:
                    updated_advance = 0
                    rent_detail.rent_status = "paid"
                else:
                    updated_advance = 0
                    rent_detail.rent_status = "due"
                print(str(updated_due)+" "+str(updated_advance))
                rent_detail.due = updated_due
                rent_detail.advance = updated_advance
                rent_detail.save()
    rents = Rent.objects.filter(user=request.user)
    context = {
        'rents': rents,
        'today_date': datetime.now().date(),
    }
    return render(request, 'user/rent.html', context)


def payrent(request, room_tag):
    if request.method == 'POST':
        rent = Rent.objects.get(room_tag=room_tag)
        advance = rent.advance
        due = rent.due
        amountpaid = rent.amount_paid
        advance_data = int(request.POST.get('advance'))
        due_data = int(request.POST.get('due'))
        amountpaid_data = int(request.POST.get('amountgiven'))
        if (request.POST.get('datepaid')) == str(datetime.now().date()):
            rent.date_paid = datetime.now().date()
        else:
            return redirect('rent')
        if advance_data == rent.advance:        
            if due_data == rent.due:
                if advance > 0:
                    rent.advance = advance + amountpaid_data
                    rent.due = 0
                    rent.rent_status = "advance"
                    print("I am god")
                elif advance == 0 and ((amountpaid_data - due) < 0):
                    rent.due = due - amountpaid_data
                    rent.rent_status = "due"
                    print("I am god1")
                elif advance == 0 and ((amountpaid_data - due) > 0):
                    rent.advance = amountpaid_data - due
                    rent.rent_status = "advance"
                    print("I am god2")
                else: # advance == 0 and ((amountpaid_data - due) == 0)
                    rent.due = 0
                    rent.rent_status = "paid"
                    print("I am Inside")
        else:
            return redirect('rent')
        if amountpaid > 0:
            rent.amount_paid = amountpaid + amountpaid_data 
        else:
            rent.amount_paid = amountpaid_data
        rent.save()
    return render(request, 'index.html')
