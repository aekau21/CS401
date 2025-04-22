import sys
import json
import logging


def read_json(x):
    with open(x, 'r') as f: #opeing the file, 'R' reading
        data = json.load( f ) # loading, jsonl.load reads the variable and stores it 
        return(data) #returning


#Funtion 1: Net Profit 

def net_profit(data):
    """
    Calculates the net profit for each movie and returns the title of the movie with the highest net profit.

    Args:
        data (list of dict): A list of movie data, each containing 'budget' and 'grossWorldwide'.

    Returns:
        str: The title of the movie with the highest net profit.
    """
    movie = ""
    profit = 0

    for i in data:
        gw = i["grossWorldWide"]
        b = i["budget"]
        if gw != "" and b != "":
            
            n = (gw - b)
            logging.debug(f"Checking movie: {i['Title']}, Gross: {gw}, Budget: {b}, Net: {n}")
            if n > profit:
                movie = i["Title"]
                profit = n 

    return(movie)


#Funtion 2: Most Expensive Movie/Highest Budget 

def most_expensive_movie(data):
    """
    Finds the movie with the highest budget returns the title of the movie.

    Args:
        data (list of dict): A list of movie data, containing 'budget'.

    Returns:
        str: The title of the movie with the highest budget.
    """
    max_budget = 0
    movie_title = ""

    for movie in data:
        try:
            budget = movie.get("budget", "")
            if budget != "" and budget > max_budget:
                max_budget = budget
                movie_title = movie["Title"]
                logging.debug(f"New max found: {movie_title} with budget {max_budget}")
        except KeyError as e:
            logging.error(f"Missing expected key in movie data: {e}")
            continue

    return (movie_title, max_budget)


#Function 3: Directors Filmography

def director_films(data, director_name):
    """
    Fetches the titles of the movies directed by a specefic director. 

    Args:
        data (list of dict): A list of movie data, the name of specefic director.

    Returns:
        str: The titles of the movies directed by the specefied director.
    """
    movies = []

    for i in data:
        director = i.get("directors", "")  # Safely get the director field
        title = i.get("Title", "")
        if director and director.lower() == director_name.lower():
            movies.append(title)
            logging.debug(f"Matched director string: {title}")

    return movies



def main():

    if len(sys.argv) < 2:

        print("Error: No command line argument provided. Please provide a file name for a json file to read. i.e. python analyze_data.py data.json")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    # Access the command line argument
    output_file = sys.argv[1]
    print(output_file)
    
    # TODO: call function to read JSON file and return data
    data = read_json(output_file)

    # TODO: call function to get the movie with the largest net profit of the past 5 years
    net_profit_answer = net_profit(data)

    print( f'Movie with largest net profit: {net_profit_answer}' )

    # TODO: second function to return and print out 

    expensive_movie, budget = most_expensive_movie(data)
    print(f'Most expensive movie: {expensive_movie} with a budget of ${budget:,}')

    # TODO: third function to return and print out result

    films = director_films(data, director_name)
    print(f"Movies by Director: {films}")

if __name__ == '__main__':
    main()