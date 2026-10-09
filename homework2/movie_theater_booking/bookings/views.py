from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

# Create your views here.

# Movie viewset - provides API operations for creating, updating and deleting movies
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# SeatView viewset - provides API operations for viewing and managing seats
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# Booking viewset - provides API operations for viewing and managing bookings
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # get the seat selected for the current booking
        seat = serializer.validated_data['seat']

        # if seat is taken, prevent them from booking it
        if seat.booking_status:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({
                'seat': 'This seat is already booked.'
            })

        # save and mark seat as booked
        serializer.save()
        seat.booking_status = True
        seat.save()

# HTML for movie_list - displays movie list page
def movie_list(request):
    # retrieve all movies from database
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {
        'movies': movies
    })

# HTML for seat_booking - displays available seats and handles bookings
def seat_booking(request, movie_id):
    # find selected movie or return error if DNE
    movie = get_object_or_404(Movie, id=movie_id)
    # retrieve seats that are currently available
    seats = Seat.objects.filter(booking_status=False)

    # process form when user submits a booking
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        
        # find selected seat if available
        seat = get_object_or_404(
            Seat,
            id=seat_id,
            booking_status=False
        )

        # didn't really get to touch on this part much
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in before booking a seat.')
            return redirect('login')

        # create booking linked to user, again didn't get to the log in part
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user,
            booking_date=timezone.now()
        )

        # mark the seat as booked in database
        seat.booking_status = True
        seat.save()

        messages.success(request, 'Your seat has been booked successfully!')
        return redirect('booking_history')

    # display available seats
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

# HTML for booking_history - display booking history for the user
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })