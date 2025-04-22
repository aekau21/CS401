import json
import logging

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# Helper function to retrieve data from the movies.json file
def get_data() -> list[dict]:
    """
    Retrieve the movies dataset and return it as a list of dictionaries.

    Returns:
        data (list[dict]): A list of dictionaries containing the movies dataset.
    """
    with open('movies.json', 'r') as file:
    
        data = json.load(file)

    return data


# TODO: Add a route to return the entire dataset
@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Get all movies in the dataset.

    Returns:
        Returns the data in the proper json format.
    """
    logging.debug("Fetching all movies from the dataset.")
    try:
        data = get_data()
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error fetching all movies: {e}")
        return jsonify({"error": "Failed to retrieve movies."}), 500
    
# TODO: Add a route, or modify an existing route, to return the movies that are between a certain release year range

@app.route('/movies?start_year=int&end_year=int', methods=['GET'])
def get_movies_range():
    """
    Get all movies from a specific year range in the dataset.

    Returns:
        Returns the data in the proper json format.
    """
    logging.debug("Fetching all movies from the dataset.")
    try:
        data = get_data()
        filtered = [movie for movie in data if 2009 <= movie.get('Year', 0) <= 2012]
        return jsonify(filtered)
    except Exception as e:
        logging.error(f"Error fetching movies from range: {e}")
        return jsonify({"error": "Failed to retrieve movies."}), 500

# TODO: Add a route to return movies with more than 1 director

@app.route('/movies/co-directed', methods=['GET'])
def get_movies_multi_directors():
    """
    Get all movies with multiple directors.

    Returns:
        JSON list of movies that have 2 or more directors.
    """
    logging.debug("Fetching all movies with multiple directors.")
    try:
        data = get_data()
        filtered = [
            movie for movie in data
            if len(movie.get('directors', [])) >= 2
        ]
        return jsonify(filtered), 200
    except Exception as e:
        logging.error(f"Error fetching co-directed movies: {e}")
        return jsonify({"error": "Failed to retrieve movies."}), 500


# TODO: Add a route to return rated R movies

@app.route('/movies/mparating', methods=['GET'])
def get_movies_ratedR():
    """
    Return all movies that are rated 'R'.

    Returns:
        JSON list of all movies with MPA rating 'R'.
    """
    logging.debug("Fetching rated R movies.")

    try:
        data = get_data()

        filtered = [
            movie for movie in data
            if movie.get("MPA") == "R"
        ]

        return jsonify(filtered), 200

    except Exception as e:
        logging.error(f"Error fetching rated R movies: {e}")
        return jsonify({"error": "Failed to retrieve movies."}), 500


# TODO: Add a route to return a movie if it matches the title

@app.route('/movies/title', methods=['GET'])
def find_movie_by_title():
    """
    Return a single movie title that matches the query string.

    Query Parameters:
        title_query (str): The movie title to search for.

    Returns:
        JSON with the title or an error message.
    """
    logging.debug("Fetching a movie by title.")

    try:
        title_query = request.args.get('title_query')

        if not title_query:
            return jsonify({"error": "title_query parameter is required."}), 400

        data = get_data()

        for movie in data:
            title = movie.get("Title", "")
            if title.lower() == title_query.lower():
                return jsonify({"Title": title}), 200

        return jsonify({"message": "Movie not found."}), 404

    except Exception as e:
        logging.error(f"Error fetching movie title: {e}")
        return jsonify({"error": "Failed to retrieve movie."}), 500

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


    