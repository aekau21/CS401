import pytest
from app import app


# TODO: write a test for the entire dataset route

def test_get_movies():
    # Create a test client using the Flask app
    client = app.test_client()

    # Make a GET request to the /movies route
    response = client.get('/movies')

    # Assert status code is 200
    assert response.status_code == 200

    # Assert that response is a list and has at least one item
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "Title" in data[0]

# TODO: write a test for the movies between a certain release year range route

def test_get_movies_range():
    # Create a test client using the Flask app
    client = app.test_client()

    # Make a GET request with actual integers for the query parameters
    response = client.get('/movies?start_year=2009&end_year=2012')

    # Assert status code is 200
    assert response.status_code == 200

    # Assert the response is a non-empty list of movies
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "Title" in data[0] or "title" in data[0]  # depending on how your JSON keys are named


# TODO: write a test for the movie by id route

from app import app

def test_get_movies_multi_directors():
    # Create test client
    client = app.test_client()

    # Send GET request to the route
    response = client.get('/movies/co-directed')

    # Check that the request was successful
    assert response.status_code == 200

    # Get the JSON response
    movies = response.get_json()

    # Assert it's a list
    assert isinstance(movies, list)

    # Check each movie has 2 or more directors
    for movie in movies:
        assert "directors" in movie
        assert isinstance(movie["directors"], list)
        assert len(movie["directors"]) >= 2


# TODO: write a test for MPA ratings, specifically rated R movies

def test_get_movies_ratedR():
    client = app.test_client()

    response = client.get('/movies/mparating')
    assert response.status_code == 200

    movies = response.get_json()
    assert isinstance(movies, list)

    for movie in movies:
        assert "MPA" in movie
        assert movie["MPA"] == "R"

# TODO: write a test for the movie by title route

def test_find_movie_by_title():
    # Create test client
    client = app.test_client()

    # Exact title from the dataset
    expected_title = "Demon Slayer: Kimetsu no Yaiba - The Movie: Mugen Train"

    # Make GET request
    response = client.get(f'/movies/title?title_query={expected_title}')

    # Check status code
    assert response.status_code == 200

    # Get JSON response
    data = response.get_json()

    # Confirm title is returned correctly
    assert "Title" in data
    assert data["Title"] == expected_title
