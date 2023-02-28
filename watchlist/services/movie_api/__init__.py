from .tmdb_api import TmdbAPI
from .omdb_api import OmdbAPI


# a method that imports another method:
def search(movie_name, page_num):
    results = TmdbAPI.search(movie_name, page_num)

    # convert tmdb search results into our way of presenting the data (if needed)

    return results

def get(tmdb_id):
    tmdb_result = TmdbAPI.get(tmdb_id)
    omdb_result = OmdbAPI.get(tmdb_result["imdb_id"])

    # if not all needed keys are exist - throw an error

    return {
        "name":tmdb_result["title"],
        "director":omdb_result.get("Director", None),

        "genres": get_genres_as_string(tmdb_result["genres"]),

        "year": tmdb_result["release_date"][:4],
        "description": tmdb_result["overview"],
        "imdb_id": tmdb_result["imdb_id"],
        "imdb_score": omdb_result["imdbRating"],

        "rotten_tomatoes_score":OmdbAPI.get_rt_rating(omdb_result['Ratings']),

    }



def get_genres_as_string(genres):

    # return ", ".join([genre["name"] for genre in genres])

    genre_names = []
    for genre in genres:
            genre_names.append(genre["name"])

    return ", ".join(genre_names)

