Movie API - Homework 4

This project contains a Flask-based web API that reads movie data from a movies.json file. The API supports multiple endpoints for filtering and retrieving movies based on various criteria.

#Build and Setup

Set up virtual enviroment in terminal :
python3 -m venv imdb

Load virtual enviroement:
source imdb/bin/activate # mac/linux
imdb\Scripts\activate # Windows

Make sure requirments is installed: 
pip install -r requirements.txt

Make sure pytest is installed

Route 1: Get All Movies
GET /movies
Loads the entire dataset.
Returns a list of all movies in JSON format.

Route 2: Movies by Year Range
GET /movies?start_year=int&end_year=int
Currently hardcoded to return movies between 2009 and 2012.
Intended to demonstrate filtering by release year.

Route 3: Movies with Multiple Directors
GET /movies/co-directed
Filters movies where the directors list contains 2 or more names.
Returns a list of co-directed movies.

Route 4: Rated R Movies
GET /movies/mparating
Filters and returns all movies with an MPA rating of "R".
Case-sensitive match against the "MPA" field.

Route 5: Find Movie by Title
GET /movies/title'
Performs a case-insensitive match on the "Title" field.
Returns the matched movie if found, or a 404 error message.

Test by running pytest in terminal

Builds the Docker image
docker build -t flask-movies-app -f dockerfile-movies

Runs the Docker container
docker run --rm -p 5000:5000 flask-movies-app