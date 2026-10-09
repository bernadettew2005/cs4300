from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Movie, Seat, Booking
from rest_framework.test import APIClient

# Create your tests here.

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date="2025-01-01",
            duration=120,
        )

    def test_movie_title(self):
        self.assertEqual(self.movie.title, "Test Movie")

    def test_movie_string_representation(self):
        self.assertEqual(str(self.movie), "Test Movie")


class MovieListViewTest(TestCase):
    def test_movie_list_page_loads(self):
        response = self.client.get(reverse("movie_list"))
        self.assertEqual(response.status_code, 200)

    def test_movie_appears_on_page(self):
        Movie.objects.create(
            title="Test Movie",
            description="A movie for testing.",
            release_date="2025-01-01",
            duration=120,
        )

        response = self.client.get(reverse("movie_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")


class SeatModelTest(TestCase):
    def test_seat_can_be_created_as_available(self):
        seat = Seat.objects.create(
            seat_number="Z1",
            booking_status=False,
        )

        self.assertEqual(seat.seat_number, "Z1")
        self.assertFalse(seat.booking_status)
        
class APIIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_movies_api_returns_200(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)

    def test_seats_api_returns_200(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)

    def test_bookings_api_returns_200(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)

    def test_movies_api_creates_movie(self):
        movie_data = {
            'title': 'Integration Test Movie',
            'description': 'Testing movie creation through the API.',
            'release_date': '2025-01-01',
            'duration': 100,
        }

        response = self.client.post(
            '/api/movies/',
            movie_data,
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Movie.objects.filter(title='Integration Test Movie').exists()
        )