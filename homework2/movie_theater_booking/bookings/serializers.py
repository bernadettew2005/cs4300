# serializers convert model objects into data that can be sent through the API

from rest_framework import serializers
from .models import Movie, Seat, Booking

# MovieSerializer - converts model objects to API data
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# SeatSerializer - converts seat objects to API data
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

# BookingSerializer - converts booking objects to API data
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'