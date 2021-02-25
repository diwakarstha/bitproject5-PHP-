from .models import report
from rooms.models import Room
from complaint.forms import reportForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from user.decorators import unauthenticated_user, allowed_users

@allowed_users(allowed_roles=['rento_admin'])
def admincomplaint(request):
    reports = report.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'useradmin/admincomplaint.html',context)


def reportcreate(request, pk):
    if request.method == 'POST':
        reportform = reportForm(request.POST)
        if reportform.is_valid():
            data = report()

            data.room = Room.objects.get(id=pk)
            data.report_type = reportform.cleaned_data['report_type']
            data.report_description = reportform.cleaned_data['report_description']
            data.save()
            return redirect('roomdetail', pk)
        return redirect('roomdetail', pk)
