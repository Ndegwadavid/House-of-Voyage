from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Station)
admin.site.register(VirtualTour)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(BookingStatus)
admin.site.register(StationVideo)
admin.site.register(StationImage)

