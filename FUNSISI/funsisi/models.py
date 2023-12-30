from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class StationImage(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stationimages')
    def __str__(self):
        return self.station.name + " - " + self.image.name[:20] + "..."  # Limit the length of the image name to 20 characters for display purposes.
    def get_absolute_url(self):
        return f"/station/{self.station.id}/"  # Return the URL of the station page for the station associated with this image.
    def get_image_url(self):
        return self.image.url  # Return the URL of the image itself.
    def get_thumbnail_url(self):
        return self.image.url  # Return the URL of the image itself.
    def get_thumbnail_url(self):
        return self.image.url  # Return the URL of the image itself.
    def get_thumbnail_url(self):
        return self.image.url  # Return the URL of the image itself.

class StationVideo(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    video = models.FileField(upload_to='stationvideos')
    def __str__(self):
        return self.station.name + " - " + self.video.name[:20] + "..."  # Limit the length of the video name to 20 characters for display purposes.
    def get_absolute_url(self):
        return f"/station/{self.station.id}/"  # Return the URL of the station page for the station associated with this video.
    def get_video_url(self):
        return self.video.url  # Return the URL of the video itself.
    def get_thumbnail_url(self):
        return self.video.url  # Return the URL of the video itself.
    def get_thumbnail_url(self):
        return self.video.url  # Return the URL of the video itself.
    def get_thumbnail_url(self):
        return self.video.url  # Return the URL of the video itself.

class VirtualTour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='virtualtours')
    duration = models.DurationField()
    def __str__(self):
        return self.name
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    virtualtour = models.ForeignKey(VirtualTour, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    date_booked = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.virtualtour.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    UserProfile = models.ImageField(upload_to='userprofile')
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class BookingStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_by')
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deleted_by')
    def __str__(self):
        return self.name
