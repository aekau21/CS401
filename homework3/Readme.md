# Homework 3

#Build and Setup

Set up virtual enviroment in terminal :
python3 -m venv imdb

Load virtual enviroement:
source imdb/bin/activate # mac/linux
imdb\Scripts\activate # Windows

Make sure requirments is installed: 
pip install -r requirements.txt

Make sure pytest is installed

This project contains a Python script that analyzes movie data from a JSON file. The script supports command-line interaction and includes three core functions for extracting insights.


Function 1: Net Profit
net_profit(data)
Iterates through the list of movie data.
Calculates the net profit for each movie as grossWorldWide - budget.
Identifies the movie with the highest net profit.
Returns the title of that movie.



Function 2: Most Expensive Movie
most_expensive_movie(data)
Loops through all movie entries.
Tracks the highest budget encountered.
Returns the title of the most expensive movie and its budget as a tuple.



Function 3: Director's Filmography
director_films(data, director_name)
Searches for movies directed by a specific person.
Performs a case-insensitive match on the directors field.
Returns a list of movie titles directed by the given name.

The analyze_data script contains the three custom functions listed above. 

The test_analyze_data.py script then tests the functions to ensure they are working correctly. 

To test the apps, run pytest in terminal. 


docker build -t movie-analyzer -f dockerfile

docker run --rm -p 5000:5000 movie-analyzer
