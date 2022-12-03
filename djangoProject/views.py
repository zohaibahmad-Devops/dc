from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect

from djangoProject.models import dc_avail

def index_view(request):
    return render(request, 'index.html')


def dc_avail_view(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        doctorname = request.POST.get('doctorname')
        timeslot = request.POST.get('timeslot')
        availability = dc_avail.objects.create(fullname=fullname,doctorname=doctorname,timeslot=timeslot)

    return render(request, 'availability_of_doctor.html')

def login_view(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('index')
        else :
            messages.Error(request, "Invalid username/password.")
    return render(request, 'login.html')