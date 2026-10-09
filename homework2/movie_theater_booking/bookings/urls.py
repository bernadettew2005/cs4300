from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

router = DefaultRouter()

router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path('booking-history/', booking_history, name='booking_history'),
]