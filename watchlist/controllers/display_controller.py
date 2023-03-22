from .. import models
from ..services import ui_service
from ..services import util



def display(
    movie_titles=[], # could be a list, all the movies with these names should return
    directors=[], # could be a list, all the movies of these directors should return
    genres=[], # could be a list, all the movies with these genres should return

    imdb_ids=[], # could be a list, all the movies with these ids should return

    year=None, # this value will be the minimum year to filter by
    imdb_rating=None, # this value will be the minimum rating to filter by
    rt_rating=None, # this value will be the minimum rating to filter by

    watched=None, # boolean option
    ):

    args = locals().items()

    where_config = {
        "movie_titles": {"column": "title", "operator": "like"},
        "directors": {"column": "director", "operator": "like"},
        "genres": {"column": "genres", "operator": "like"},
        "imdb_ids": {"column": "imdb_ids", "operator": "equals"},
        "year": {"column": "year", "operator": "gte"},
        "imdb_rating": {"column": "imdb_score", "operator": "gte"},
        "rt_rating": {"column": "rotten_tomatoes_score", "operator": "gte"},
    }

    filters = []
    for key, value in args:
        if value:
            filters.extend(util.where_condition_looping(value, where_config[key]["column"], where_config[key]["operator"]))

    print(filters)



    # if movie_title:
    #     results = models.find_movies_by_title(movie_title)

    # if imdb_id:
    #     results = models.find_movie_by_imdb_id(imdb_id)

    # else:
    #     results = models.find_all_movies(filters=filters)


def interactive_selection_menu():
    pass


#TODO: continue with the flow
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