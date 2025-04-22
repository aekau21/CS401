from analyze_data import net_profit
from analyze_data import most_expensive_movie
from analyze_data import director_films

import pytest

def test_net_profit():
    # TODO: write unit tests for net profit function 
    ds = [{"Title": "Avatar", "grossWorldWide": 1000000, "budget": 1000000},
          {"Title": "GiJoe", "grossWorldWide": 500000, "budget": 5000000},
          {"Title": "Max", "grossWorldWide": 150000000000, "budget": 123}
          ]
    assert(net_profit(ds)) == "Max"

# TODO: write unit tests for second function in analyze_data.py

def test_most_expensive_movie():
    # TODO: write unit tests for budget  function 
    ds_1 = [{"Title": "Avatar", "budget": 1000000},
          {"Title": "GiJoe", "budget": 5000000},
          {"Title": "Max", "budget": 123}
          ]
    assert most_expensive_movie(ds_1) == ("GiJoe", 5000000)



# TODO: write unit tests for second function in analyze_data.py

def test_director_films():
    # TODO: write unit tests for budget  function 
    ds_2 = [{"Title": "Inception", "directors": "Christopher Nolan"},
          {"Title": "Interstellar", "directors": "Christopher Nolan"},
          {"Title": "Falling", "directors": "Viggo Mortensen"}
          ]
    assert director_films(ds_2, "Christopher Nolan") == ["Inception", "Interstellar"]