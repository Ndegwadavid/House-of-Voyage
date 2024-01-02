from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Station, StationImage, VirtualTour, Booking
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


# Create your views here.


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user_name = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']

        new_user = User.objects.create_user(user_name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('success')

    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
@login_required(login_url='login')
def dashboard(request):
    stations = Station.objects.all()
    return render(request, 'dashboard.html', {'stations': stations} )

def my_account(request):
    return render(request, 'my_account.html')

def my_bookings(request):
    return render(request, 'my_bookings.html')

def stations(request):
    stations = Station.objects.all()
    return render(request, 'stations.html', {'stations': stations})

def book_station(request):
    return render(request, 'book_station.html', {'station': StationImage})

def book_virtual_tour(request, virtual_tour_id):
    virtual_tour = VirtualTour.objects.get(id=virtual_tour_id)
    return render(request, 'book_virtual_tour.html', {'virtual_tour': virtual_tour})
    if request.method == 'POST':
        booking = Booking(user=request.user, station=station, virtual_tour=virtual_tour)
        booking.save()
        return render(request, 'booking_success.html')
    
    return render(request, 'funsisi/book_virtual_tour.html', {'virtual_tour': virtual_tour})