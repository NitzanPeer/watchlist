from ..services import util
from ..services.mysql_service import MySQLService
from typing import Any


table_name = "movies"
create_table_query = \
f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT NOT NULL AUTO_INCREMENT,
        title VARCHAR(50) NOT NULL,
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

def __find_movie_by_column(column_name, column_value, columns=[], one_result = False, operator="="):

    if operator == "like":
        column_value = f"%{column_value}%"

    where_condition = MySQLService.create_where_data(column_name, operator, column_value)

    if one_result:
        result = mysql_service.select_one(table_name, columns, where_data=where_condition)
    else:
        result = mysql_service.select_all(table_name, columns, where_data=where_condition)

    return result

def add_movie(title, year, director, genres, imdb_id, imdb_score, rotten_tomatoes_score, description):

    movie_info = {
        'title': title,
        'year': year,
        'director': director,
        'genres': genres,
        'imdb_id': imdb_id,
        'imdb_score': imdb_score,
        'rotten_tomatoes_score': rotten_tomatoes_score,
        'description': description,
    }

    return mysql_service.insert(table_name, movie_info)

def delete_movie_by_id(id):

    where_condition = MySQLService.create_where_data("id", "=", id)

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

    where_condition = MySQLService.create_where_data("id", "=", id)

    result = mysql_service.update(table_name, set_data, where_condition)
    return result

def find_all_movies_join_watch_status(where_config={}, args=[]):

    where_data = []
    for key, value in args:
        if value or isinstance(value, bool):
            where_data.extend(MySQLService.create_multiple_where_data(value, where_config[key]["column"], where_config[key]["operator"]))

    join_data = {
        "target_table": "watch_status",
        "source_column": "id",
        "target_column": "movie_id"
     }

    columns = [
        "movies.*", "watch_status.watch_status"
    ]

    return mysql_service.select_all(table_name, columns, join_data=join_data, where_data=where_data, order_by_columns=[], limit={})


def find_movies_by_title(movie_title, columns=[]):

    return __find_movie_by_column('title', movie_title, columns, operator="like")




# funcs that aren't in use anywhere:

def find_movie_by_id(movie_id, columns=[]):

    return __find_movie_by_column('id', movie_id, columns, True)

def find_movie_by_imdb_id(imdb_id, columns=[]):

    return __find_movie_by_column('imdb_id', imdb_id, columns, True)

def create_table_if_not_exist():
    if not is_table_exist('movies'):
        mysql_service.raw_query(create_table_query)

def is_table_exist(table_name):
    return mysql_service.is_table_exist(table_name)
