from .. import models
from ..services import ui_service
from ..services import util



def display(
    movie_title=None, # could be a list, all the movies with these names should return
    director=None, # could be a list, all the movies of these directors should return
    genre=None, # could be a list, all the movies with these genres should return

    imdb_id=None, # could be a list, all the movies with these ids should return

    year=None, # this value will be the minimum year to filter by
    imdb_rating=None, # this value will be the minimum rating to filter by
    rt_rating=None, # this value will be the minimum rating to filter by

    watched=None, # boolean option
    ):

    print("display start")

    where_clause1 = where_condition_looping_for_like_operator(movie_title)
    where_clause2 = where_condition_looping_for_like_operator(director)
    where_clause3 = where_condition_looping_for_like_operator(genre)

    where_clause4 = where_condition_looping_for_bigger_or_equal_operators(year)
    where_clause5 = where_condition_looping_for_bigger_or_equal_operators(imdb_rating)
    where_clause6 = where_condition_looping_for_bigger_or_equal_operators(rt_rating)

    where_clause7 = where_condition_looping_for_equal_operator(imdb_id)

    combined_clause = where_clause1 + where_clause2 + where_clause3 + where_clause4 + where_clause5 + where_clause6 + where_clause7
    print(combined_clause)



    # if movie_title:
    #     results = models.find_movies_by_title(movie_title)

    # if imdb_id:
    #     results = models.find_movie_by_imdb_id(imdb_id)

    # else:
    #     results = models.find_all_movies(filters=filters)


def interactive_selection_menu():
    pass




def where_condition_looping_for_like_operator(list_of_items):
    result_clause = []
    print(result_clause)

    for item in list_of_items:
        result_clause.append(util.where_condition_handling(f"{item}", 'LIKE', '%' + item + '%'))

    return result_clause

def where_condition_looping_for_bigger_or_equal_operators(list_of_items):
    result_clause = []

    for item in list_of_items:
        result_clause.append(util.where_condition_handling(f"{item}", '>=', item))

    return result_clause

def where_condition_looping_for_equal_operator(list_of_items):
    result_clause = []

    for item in list_of_items:
        result_clause.append(util.where_condition_handling(f"{item}", '=', item))

    return result_clause



quit()




# the flow can be started in multiple ways:
    # the user enters the run cmd the movie title
    # the user enters the run cmd the movie imdb id
    # the user does not enters anything extra into the run cmd (show all movies)
# the user can add filters to the display so the results will be filtered with the user's input
# get results from db based on the user's input
# print the results (all the info we got, including status!!! = mysql join)




# python -m watchlist display --director="Ben Stiller" --director="Clint Eastwood"


# request1
# python -m watchlist display --title="titanic" --genre="thriller" --imdb_s=7.5

# query1
# SELECT * FROM movies WHERE title LIKE '%titanic%' AND genres LIKE '%Thriller%' AND imdb_score > 7.5;


# request2
# python -m watchlist display --genre="drama" --genre="action"

# query1
# SELECT * FROM movies WHERE


display(director=["Ben Stiller", "Clint Eastwood"], genres=['thriller', 'action'])

director_clause1 = util.where_condition_handling('director', 'LIKE', '%' + director[0] + '%')
director_clause2 = util.where_condition_handling('director', 'LIKE', '%' + director[1] + '%')

all_director_clause = []
all_director_clause = all_director_clause + director_clause1
all_director_clause = all_director_clause + director_clause2

all_director_clause = [
    {},
    {}
]



[
    [
        {},
        {}
    ]
]

movie_title
imdb_id
director
genre
year
imdb_rating
rt_rating
watched




filters = [movie_title, imdb_id, director, genre, year, imdb_rating, rt_rating, watched]

where_list_of_dicts = []

for filter_list in filters:
    where_dict = []
    for filter in filter_list:
        if filter:
            where_dict = {
                f"{filter_list}": filter
        }
    where_list_of_dicts.append(where_dict)