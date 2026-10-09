import os
import django
from django.conf import settings

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "movie_theater_booking.settings"
)

django.setup()

settings.ALLOWED_HOSTS = list(settings.ALLOWED_HOSTS) + ["testserver"]