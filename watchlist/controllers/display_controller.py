from .. import models
from ..services import ui_service
from ..services import util
from ..services.mysql_service import MySQLService

mysql_service = MySQLService()


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
        "imdb_ids": {"column": "imdb_id", "operator": "equals"},
        "year": {"column": "year", "operator": "gte"},
        "imdb_rating": {"column": "imdb_score", "operator": "gte"},
        "rt_rating": {"column": "rotten_tomatoes_score", "operator": "gte"},
        "watched": {"column": "watch_status", "operator": "equals"}
    }

    search_results = models.find_all_movies_join_watch_status(where_config, args)

    print(f"search_results = {search_results}\n")


    # TABULATE:
    # with the id column:
    # ui_service.print_options_table(["id", "title", "director", "genres", "year", "description", "imdb id", "imdb score", "rt score", "watched"], search_results)

    # without the id column:

    for result in search_results:
         del result["id"]
         del result["description"]

    ui_service.print_options_table(["title", "director", "genres", "year", "imdb id", "imdb score", "rt score", "watched"], search_results)













# funcs that participate and need to include a watched flag:
# __raw_select in mysql_service
# select_all
# select_one(?)
# find_all_movies
# others prob






#TODO: continue with the flow
# the flow can be started in multiple ways:
    # the user enters the run cmd the movie title
    # the user enters the run cmd the movie imdb id
    # the user does not enter anything extra into the run cmd (show all movies)
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




# MIGHT USE LATER:



    # select * from movies and watch_status column from watch_status:
    # SELECT movies.*, watch_status.watch_status FROM movies JOIN watch_status ON movies.id = watch_status.movie_id;
    # SELECT movies.*, watch_status.watch_status FROM movies JOIN watch_status ON movies.id = watch_status.movie_id WHERE (title LIKE '%Titanic%') AND (watch_status = 1);


    # filters = list of lists?
    # [[matrix, titanic], [action, drama], [year]]

    # filters = list of dicts?
    # [
    #   {
    #       "movie_title":
    #   }
    # ]

    # where_data = []

    # for list_of_filters in filters:
    #     for item in list_of_filters:
    #         {
    #             'column': 'title',
    #             'operator': '=',
    #             'value': 'matrix'
    #         },
    #         {
    #             'column': 'title',
    #             'operator': '=',
    #             'value': 'titanic'
    #         },
    #         {
    #             'column': 'year',
    #             'operator': '>',
    #             'value': 1998
    #         }






    # this menu was created because (AFAIK) we can't really know if the user entered a movie title or an imdb_id
    # unless we search for what he entered in all the titles and all the imdb_ids we have

    # print("1. Search movie by title")
    # print("2. Search movie by IMDB id")
    # print("3. Search the entire database")
    # print("4. Quit")

    # choice = input("Please choose a search method:")


    # if choice == 1:
    #     results = models.find_movies_by_title(movie_titles)

    # if choice == 2:
    #     results = models.find_movie_by_imdb_id(imdb_ids)

    # if choice == 3:
    #     quit()