from ..services import exceptions
from .. import models
from ..services import ui_service
from ..services import util


def delete(movie_title):

    movie_id = interactive_selection_menu(movie_title)

    models.delete_movie_by_id(movie_id)
    ui_service.print_delete_movie_summary(movie_title)

def interactive_selection_menu(movie_title):

    movies_found = models.find_movies_by_title(movie_title)

    if not movies_found:
        raise exceptions.NoMoviesFoundError(f"No movies named {movie_title} were found.")

    extracted_data = util.extract_title_and_year(movies_found)
    ui_service.print_options_table(["title", "year"], extracted_data)

    if len(movies_found) == 1:

        query = "Is this the movie you were looking for? (enter 'y' or 'n')"

        if ui_service.confirm_choice(query):
            movie_id = movies_found[0]['id']

        else:
            raise exceptions.NoMoviesFoundError(f"No movies were found.")

    elif len(movies_found) > 1:

            query = "Choose an option number:"

            movie_id = ui_service.get_valid_chosen_option_from_options(movies_found, query)['id']


    return movie_id
