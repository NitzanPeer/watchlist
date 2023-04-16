from ..services import util
from ..services.mysql_service import MySQLService
from ..services import exceptions

table_name = "watch_status"
create_table_query = \
f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
	id INT NOT NULL AUTO_INCREMENT,
	movie_id INT NOT NULL,
    watch_status TINYINT(1),
	PRIMARY KEY(id)
    );
"""

mysql_service = MySQLService()

def add_watch_status(movie_id, watch_status):

    movie_data = {
        'movie_id': int(movie_id),
        'watch_status': int(watch_status)
    }

    result = mysql_service.insert(table_name, movie_data)
    return result

def update_watch_status(movie_id, watch_status):

    if is_watched(movie_id) == watch_status:
        status = '"Watched"' if watch_status else '"Not Watched"'
        raise exceptions.StatusAlreadyMarkedThatWay(f"Status is already marked as {status}.")

    set_data = {'watch_status': int(watch_status)}

    where_condition = MySQLService.create_where_data("movie_id", "=", movie_id)

    result = mysql_service.update(table_name, set_data, where_condition)
    return result

def mark_as_watched(movie_id):
    return update_watch_status(movie_id, True)

def mark_as_unwatched(movie_id):
    return update_watch_status(movie_id, False)

def get_watch_status_by_movie_id(movie_id):

    where_condition = MySQLService.create_where_data("movie_id", "=", movie_id)

    columns = ['watch_status']

    #TODO: test prints:

    print(f"RESULT ==== {table_name, columns, where_condition}")

    result = mysql_service.select_one(table_name, columns, where_data = where_condition)

    print(f"RESULT ==== {result}")


    return bool(result['watch_status']) if result else None

def is_watched(movie_id):
    return get_watch_status_by_movie_id(movie_id)



# funcs that aren't in use:

def create_table_if_not_exist():
    if not is_table_exist('watch_status'):
        mysql_service.raw_query(create_table_query)

def is_table_exist(table_name):
    return mysql_service.is_table_exist(table_name)

def delete_watch_status_by_movie_id(movie_id):

    where_condition = MySQLService.create_where_data("movie_id", "=", movie_id)

    result = mysql_service.delete(table_name, where_condition)
    return result