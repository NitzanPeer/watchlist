from .. import models
from ..services import ui_service
from ..services import util

def display(

        movie_title=None, # could be a list, all the movies with these names should return
        imdb_id=None, # could be a list, all the movies with these ids should return
        director=None, # could be a list, all the movies of these directors should return
        genre=None, # could be a list, all the movies with these genres should return

        year=None, # this value will be the minimum year to filter by
        imdb_rating=None, # this value will be the minimum rating to filter by
        rt_rating=None, # this value will be the minimum rating to filter by

        watched=None, # boolean option
    ):


    # the flow can be started in multiple ways:
        # the user enters the run cmd the movie title
        # the user enters the run cmd the movie imdb id
        # the user does not enters anything extra into the run cmd (show all movies)
    # the user can add filters to the display so the results will be filtered with the user's input
    # get results from db based on the user's input
    # print the results (all the info we got, including status!!! = mysql join)


    filters = [
        util.where_condition_handling(....)
    ]


    if movie_title:
        results = models.find_movies_by_title(movie_title)

    if imdb_id:
        results = models.find_movie_by_imdb_id(imdb_id)

    else:
        results = models.find_all_movies(filters=filters)


def interactive_selection_menu():
    pass
