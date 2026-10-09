from behave import when, then
from django.test import Client


@when("the visitor opens the movie list page")
def open_movie_list(context):
    context.client = Client()
    context.response = context.client.get("/movies/")


@then("the page should load successfully")
def check_movie_list(context):
    assert context.response.status_code == 200, (
        f"Expected 200, got {context.response.status_code}"
    )