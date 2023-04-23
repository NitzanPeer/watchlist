from .tmdb_api import TmdbAPI
from .omdb_api import OmdbAPI


def search(movie_name, page_num):
    results = TmdbAPI.search(movie_name, page_num)

    return results

def get(tmdb_id):
    tmdb_result = TmdbAPI.get(tmdb_id)
    omdb_result = OmdbAPI.get(tmdb_result["imdb_id"])


    return {
        "title":tmdb_result["title"],
        "director":omdb_result.get("Director", None),

        "genres": get_genres_as_string(tmdb_result["genres"]),

        "year": int(tmdb_result["release_date"][:4]),
        "description": tmdb_result["overview"],
        "imdb_id": tmdb_result["imdb_id"],
        "imdb_score": float(omdb_result["imdbRating"]),

        "rotten_tomatoes_score":OmdbAPI.get_rt_rating(omdb_result['Ratings'])
    }

def get_genres_as_string(genres):

    genre_names = []
    for genre in genres:
            genre_names.append(genre["name"])

    return ", ".join(genre_names)

