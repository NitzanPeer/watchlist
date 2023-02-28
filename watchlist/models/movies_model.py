from ..services.mysql_service import MySQLService
from typing import Any


# in the controller we use the tmdb search method to present the user with options
# user chooses an options and we get the tmdb_id of it which will fuel the funcs:

# table = 'movies'
# tmdb_id = 69
# tmdb_json = TmdbAPI.get(tmdb_id)
# omdb_json = OmdbAPI.get(tmdb_json['imdb_id'])

table_name = "movies"
create_table_query = \
f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        director VARCHAR(50),
        genres VARCHAR(50),
        year YEAR,
        description TEXT,
        imdb_id VARCHAR(11),
        imdb_score FLOAT(3),
        rotten_tomatoes_score INT,
        PRIMARY KEY(id)
    );
"""

mysql_service = MySQLService()

def where_condition_handling(column:str, operator:str, value:Any) -> int:

    return [
        {
            'column': column,
            'operator': operator,
            'value': value
        }
    ]

def __find_movie_by_column(column_name, column_value, columns=[]):

    where_condition = where_condition_handling(column_name, "=", column_value)
    result = mysql_service.select_one(table_name, columns, where_data=where_condition)

    return result

def add_movie(name, year, director, genres, imdb_id, imdb_score, rotten_tomatoes_score, description):

    genres_one_string = ", ".join(genres)

    movie_info = {
        'name': name,
        'year': year,
        'director': director,
        'genres': genres_one_string,
        'imdb_id': imdb_id,
        'imdb_score': imdb_score,
        'rotten_tomatoes_score': rotten_tomatoes_score,
        'description': description,
    }

    return mysql_service.insert(table_name, movie_info)

def find_all_movies(columns=[]):
    all_movies = mysql_service.select_all(table_name, columns)
    return all_movies

def find_movie_by_id(movie_id, columns=[]):

    return __find_movie_by_column('id', movie_id, columns)

def find_movie_by_imdb_id(imdb_id, columns=[]):

    return __find_movie_by_column('imdb_id', imdb_id, columns)

def find_movie_by_name(movie_name, columns=[]):

    return __find_movie_by_column('name', movie_name, columns)

def delete_movie_by_id(id):

    where_condition = where_condition_handling("id", "=", id)

    result = mysql_service.delete(table_name, where_condition)
    return result

def update_movie_scores_by_id(id, imdb_score=None, rotten_tomatoes_score=None):

    set_data = {}

    if imdb_score:
        set_data['imdb_score'] = float(imdb_score)

    if rotten_tomatoes_score:
        set_data['rotten_tomatoes_score'] = int(rotten_tomatoes_score)

    if not set_data:
        return False

    where_condition = where_condition_handling("id", "=", id)

    result = mysql_service.update(table_name, set_data, where_condition)
    return result

def create_table_if_not_exist():
    if not is_table_exist('movies'):
        mysql_service.raw_query(create_table_query)

def is_table_exist(table_name):
    return mysql_service.is_table_exist(table_name)
