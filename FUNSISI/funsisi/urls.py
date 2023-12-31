from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('stations/', views.stations, name='stations'),
    path('book_station/<int:station_id>/', views.book_station, name='book_station'),
    path('book_virtual_tour/<int:virtual_tour_id>/', views.book_virtual_tour, name='book_virtual_tour'),
]