# python -m watchlist (from projects/Python/watchlist)

import click

from .services.exceptions import MovieError
from .controllers import add_controller
from .controllers import update_controller
from .controllers import delete_controller
from .controllers import display_controller

from .models import *


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
@click.option('--title', multiple=True, default=[], type=str)
@click.option('--director', multiple=True, default=[], type=str)
@click.option('--genre', multiple=True, default=[], type=str)
@click.option('--imdb_id', multiple=True, default=[], type=str)
@click.option('--year', default=None, type=int)
@click.option('--imdb_rating', default=None, type=float)
@click.option('--rt_rating', default=None, type=int)
@click.option('--watched', default=None, type=int)
def display_movies(title, director, genre, imdb_id, year, imdb_rating, rt_rating, watched):
    display_controller.display(title, director, genre, imdb_id, year, imdb_rating, rt_rating, watched)


if __name__ == "__main__":

    try:
        watchlist_cli()
        quit()

    except MovieError as e:
        print(e)