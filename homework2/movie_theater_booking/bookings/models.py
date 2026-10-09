from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Movie model - stores info about movies available for booking
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

    # displays movie title when displayed as text
    def __str__(self):
        return self.title

# Seat model - stores seats and whether or not seat is available/has been booked
class Seat(models.Model):
    seat_number = models.CharField(max_length=200)
    booking_status = models.BooleanField()

# Booking model - records booking history
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()