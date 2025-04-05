import sys
import json

def add (x, y):
    return (x + y)



def read_json(x):
    with open(x, 'r') as f: #opeing the file, 'R' reading
        data = json.load( f ) # loading, jsonl.load reads the variable and stores it 
        return(data) #returning

    
    # TODO: read the JSON file and return the data

def net_profit(data):
    movie = ""
    profit = 0

    for i in data:
        gw = i["grossWorldWide"]
        b = i["budget"]
        if gw != "" and b != "":
            
            n = (gw - b)
            if n > profit:
                movie = i["Title"]
                profit = n 

    return(movie)




    
    
    # TODO: movie with the largest net profit of the past 5 years
    

# TODO: add second function to print out interesting statistics about the data


# TODO: add third function to print out interesting statistics about the data


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

    # TODO: third function to return and print out result


if __name__ == '__main__':
    main()