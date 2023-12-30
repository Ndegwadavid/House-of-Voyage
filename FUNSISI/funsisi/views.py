from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Station, VirtualTour, Booking
# Create your views here.


def home(request):
    return render(request, 'funsisi/index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def stations(request):
    stations = Station.objects.all()
    return render(request, 'stations.html', {'stations': stations})

def book_station(request, station_id):
    station = Station.objects.get(id=station_id)
    return render(request, 'book_station.html', {'station': station})

def book_virtual_tour(request, virtual_tour_id):
    virtual_tour = VirtualTour.objects.get(id=virtual_tour_id)
    return render(request, 'book_virtual_tour.html', {'virtual_tour': virtual_tour})
    if request.method == 'POST':
        booking = Booking(user=request.user, station=station, virtual_tour=virtual_tour)
        booking.save()
        return render(request, 'booking_success.html')
    
    return render(request, 'funsisi/book_virtual_tour.html', {'virtual_tour': virtual_tour})

