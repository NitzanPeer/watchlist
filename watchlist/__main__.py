# python -m watchlist (from projects/Python/watchlist)

import sys
import click

from .services.exceptions import MovieError
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


@click.group()
def watchlist_cli():
    pass

@watchlist_cli.command(name="add")
@click.argument('movie_title')
def add_movie(movie_title):
    add_controller.add(movie_title)

@watchlist_cli.command(name="delete")
@click.argument('movie_title')
def delete_movie(movie_title):
    delete_controller.delete(movie_title)

@watchlist_cli.command(name="update")
@click.argument('movie_title')
def update_movie(movie_title):
    update_controller.update(movie_title)

@watchlist_cli.command(name="display")
@click.option('--title', multiple=True, default=[])
@click.option('--director', multiple=True, default=[])
@click.option('--genre', multiple=True, default=[])
@click.option('--imdb_id', multiple=True, default=[])
@click.option('--year', default=None)
@click.option('--imdb_rating', default=None)
@click.option('--rt_rating', default=None)
@click.option('--watched', default=None)
def display_movies(title, director, genre, imdb_id, year, imdb_rating, rt_rating, watched):
    display_controller.display(list(title), list(director), list(genre), list(imdb_id), year, imdb_rating, rt_rating, watched)



if __name__ == "__main__":

    # TODO:
    # tabulate doesn't like nulls (FIXED with a loop in display_controller)
    # make all the abilities of display functional (DONE)


    try:

        # display = display_controller.display(directors=["Ben Stiller", "Clint Eastwood"], genres=['thriller'], imdb_ids = ["123", "1234"], imdb_rating=80, rt_rating=85)
        # display = display_controller.display(movie_titles="Titanic", watched=False)
        # display = display_controller.display(directors=[], genres=[], imdb_ids = [], imdb_rating=[], rt_rating=[])
        # update = update_controller.update("titan")

        watchlist_cli()

        quit()

        status = add_controller.add("titanic")
        update = update_controller.update("titanic")
        delete = delete_controller.delete("titanic")


    except MovieError as e:
        print(e)
        # print(dir(e))
        # print(vars(e))