from .. import models
from ..services import ui_service


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

    print(f"args = {args}")

    search_results = models.find_all_movies_join_watch_status(where_config, args)

    # TODO: test print:
    print(f"search_results = {search_results}\n")


    for result in search_results:
         del result["id"]
         del result["description"]

        # turning Nones to empty strings for tabulate:
         for key in result:
            if not result[key]:
                result[key] = ''


    ui_service.print_options_table(["title", "director", "genres", "year", "imdb id", "imdb score", "rt score", "watched"], search_results)
