from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

# Create your views here.

# Movie viewset
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# SeatView viewset
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# Booking viewset
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']

        if seat.booking_status:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({
                'seat': 'This seat is already booked.'
            })

        serializer.save()
        seat.booking_status = True
        seat.save()

# HTML for movie_list
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {
        'movies': movies
    })

# HTML for seat_booking
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(booking_status=False)

    if request.method == 'POST':
        seat_id = request.POST.get('seat')

        seat = get_object_or_404(
            Seat,
            id=seat_id,
            booking_status=False
        )

        if not request.user.is_authenticated:
            messages.error(request, 'Please log in before booking a seat.')
            return redirect('login')

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user,
            booking_date=timezone.now()
        )

        seat.booking_status = True
        seat.save()

        messages.success(request, 'Your seat has been booked successfully!')
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

# HTML for booking_history
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })