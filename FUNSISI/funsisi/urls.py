from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import login, register, success, about,  stations, book_station, book_virtual_tour, home

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('book_station/', views.book_station, name='book_station'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),    path('stations/', views.stations, name='stations'),
]