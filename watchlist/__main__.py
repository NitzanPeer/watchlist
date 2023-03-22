# python -m watchlist (from projects/Python/watchlist)

import sys
import mysql.connector
import requests

from .services.exceptions import MovieError

from .services.mysql_service import MySQLService
from .services.movie_api.tmdb_api import TmdbAPI
from .services.movie_api.omdb_api import OmdbAPI
from .controllers import add_controller
from .controllers import update_controller
from .controllers import delete_controller
from .controllers import display_controller

from .models import *


def verify_valid_command(cli_arguments):
    valid_commands = ["add", "remove", "update", "show"]
    valid_action = action in valid_commands
    valid_len = len(cli_arguments) >= 4

    return valid_action and valid_len

def handle_cli_args_example():
    if len(sys.argv) < 3:
        print("\nCommand must contain at least 3 arguments (path + 2 user entered words)")
        quit()

    # sys.argv[1:]  ?
    cli_arguments = sys.argv
    action = cli_arguments[1]
    movie_title = cli_arguments[2]
    if len(sys.argv) > 3:
        watch_status = cli_arguments[3]


print(__name__)

if __name__ == "__main__":


    # TODO: create a new flow/controller for display

    print("main")


    try:
        where_data = [
            {
                'column': 'title',
                'operator': '=',
                'value': 'the matrix'
            },
            {
                'column': 'title',
                'operator': '=',
                'value': 'titanic'
            },
            {
                'column': 'title',
                'operator': '=',
                'value': 'the matrix'
            },
            {
                'column': 'title',
                'operator': '=',
                'value': 'titanic'
            },
            {
                'column': 'year',
                'operator': '=>',
                'value': 1998
            }
        ]


        print("main")

        display = display_controller.display(director=["Ben Stiller", "Clint Eastwood"], genre=['thriller', 'action'])


        quit()

        mysql_service = MySQLService()
        asds = mysql_service.__where_clause_handling(where_data)
        print(asds)


        status = add_controller.add("titanic")
        update = update_controller.update("titanic")
        delete = delete_controller.delete("titanic")

    except MovieError as e:
        print(e)
        # print(dir(e))
        # print(vars(e))






# TODO: __find_movie_by_column should enable using LIKE as an operator
# TODO: find_movies_by_title should wrap the title in a LIKE wildcard (%)
# TODO: create a mysql method that can get filters and build a where clause from them
    # filter structure:
        # [
        #     {
        #         'column': 'director',
        #         'operator': 'LIKE',
        #         'values': ["Ben Stiller", "Clint Eastwood"]
        #     },
        #     {
        #         'column': 'title',
        #         'operator': 'LIKE',
        #         'values': ["matrix", "matrix2"]
        #     },
        #     {
        #         'column': 'year',
        #         'operator': '>=',
        #         'values': 1998
        #     },
        #     {
        #         'column': 'imdb_id',
        #         'operator': '=',
        #         'values': ['tt435', 'tt21346']
        #     }
        # ]