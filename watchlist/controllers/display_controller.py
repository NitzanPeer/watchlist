


def display(
        movie_title=None,
        imdb_id=None,
        director=None, # could be a list, all the movies of these directors should return
        genre=None, # could be a list, all the movies with these genres should return
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


    pass