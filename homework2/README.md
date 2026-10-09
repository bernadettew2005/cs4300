# Movie Theater Booking System

## Project Overview

The Movie Theater Booking System is a Django web application that allows users to view movies, check seat availability, make bookings, and review booking history. The project also provides a REST API for accessing movies, seats, and bookings.

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* HTML and CSS
* Bootstrap
* Gunicorn
* WhiteNoise
* Render

## Features

* View a list of movies.
* View available seats for a movie.
* Book seats for movies.
* Prevent booking a seat that is already booked.
* View booking history.
* Access movie, seat, and booking data through a REST API.
* Manage application data through the Django administration site.

## Application URLs

**Live Application:** https://movie-theater-booking-579p.onrender.com

| Feature               | URL                                                                                      | Description                                                            |
| --------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Movie List            | [Open Movie List](https://movie-theater-booking-579p.onrender.com/movies/)               | View the available movies.                                             |
| Seat Booking          | [Open Seat Booking](https://movie-theater-booking-579p.onrender.com/movies/1/seats/)     | View seats for movie ID 1, if that movie exists.                       |
| Booking History       | [Open Booking History](https://movie-theater-booking-579p.onrender.com/booking-history/) | View booking history.                                                  |
| Django Administration | [Open Admin](https://movie-theater-booking-579p.onrender.com/admin/)                     | Manage application data with an authorized staff or superuser account. |
| Movies API            | [Open Movies API](https://movie-theater-booking-579p.onrender.com/api/movies/)           | Access movie data through the API.                                     |
| Seats API             | [Open Seats API](https://movie-theater-booking-579p.onrender.com/api/seats/)             | Access seat data through the API.                                      |
| Bookings API          | [Open Bookings API](https://movie-theater-booking-579p.onrender.com/api/bookings/)       | Access booking data through the API.                                   |

**Note:** The main movie-list page is `/movies/`. The root URL (`/`) may return a 404 error if a homepage route has not been configured.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bernadettew2005/cs4300.git
cd cs4300/homework2/movie_theater_booking
```

Adjust the `cd` command if your terminal starts in a different directory.

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

Migrations create and update the database tables required by the application.

### 5. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create an account for Django administration.

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/movies/ in your browser.

## Running Tests

Run the Django test suite with:

```bash
python manage.py test
```

## API Endpoints

* `/api/movies/` — movie records.
* `/api/seats/` — seat records.
* `/api/bookings/` — booking records.

Available operations depend on the configured viewsets, serializers, and permissions.

## Deployment

The application is deployed using Render.

* **Root Directory:** `homework2/movie_theater_booking`

* **Build Command:**

  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```

* **Start Command:**

  ```bash
  gunicorn movie_theater_booking.wsgi:application
  ```

**Live URL:** https://movie-theater-booking-579p.onrender.com

## AI Usage Disclosure

AI tools, including ChatGPT, were used as learning and development aids during this project. They helped explain Django concepts, troubleshoot configuration and deployment issues, clarify database migrations and commands, and assist with documentation.

AI-generated explanations and suggestions were reviewed and adapted as needed to support the project's implementation.

## Security Notes

* Do not commit production secret keys or other credentials to the repository.
* Configure production settings using environment variables.
* Use an authorized administrator account to access Django administration.
* Review Django's deployment security settings before using the application in a production environment.
