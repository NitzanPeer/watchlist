# python -m watchlist (from projects/watchlist)

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

from .models import *
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
    movie_name = cli_arguments[2]
    if len(sys.argv) > 3:
        watch_status = cli_arguments[3]

if __name__ == "__main__":


    try:

        status = add_controller.add("titanic")
        # update = update_controller.update("titanic")
        # delete = delete_controller.delete("titanic")

    except MovieError as e:
        print(e)
        # print(dir(e))
        # print(vars(e))

