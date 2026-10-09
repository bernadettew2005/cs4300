from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    
    def __str__(self):
        return self.title

# Seat model
class Seat(models.Model):
    seat_number = models.CharField(max_length=200)
    booking_status = models.BooleanField()

# Booking model
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()