from ..services import exceptions
from .. import models
from ..services import ui_service
from ..services import util


def delete(movie_name):
    # # we use the movie_name to select all the movies with said name and show the user
    # if empty list raise exception (which the main will catch)
    # if one result - show confirmation screen (is this the movie you wanted?)
        #  yes - continue with said movie
        #  no - raise exception (similar to no result)
    # if more than one result - show results and let the user pick between them

    # delete relevant movie in movies AND watch_status (IF NOT DELETED AUTO, CHECK IT WITH A MYSQL QUERY)
    # show summary of action

    movie_id = interactive_selection_menu(movie_name)

    models.delete_movie_by_id(movie_id)
    ui_service.print_delete_movie_summary(movie_name)


def interactive_selection_menu(movie_name):
    # validation? what if not a list?

    movies_found = models.find_movie_by_name(movie_name)

    if not movies_found:
        raise exceptions.NoMoviesFoundError(f"No movies named {movie_name} were found.")

    print_worthy_list = []
    for movie in movies_found:
        print_worthy_list.append({'name': movie['name'], 'year': movie['year']})

    ui_service.print_options_table(["name", "year"], print_worthy_list)


    if len(movies_found) == 1:

        query = "Is this the movie you were looking for? (enter 'y' or 'n')"

        if ui_service.confirm_choice(query):
            movie_id = movies_found[0]['id']

        else:
            raise exceptions.NoMoviesFoundError(f"No movies were found.")


    elif len(movies_found) > 1:

            # repeated, move to util:
            int_list = list(range(1, len(movies_found)+1))
            valid_choices = list(map(lambda a : str(a), int_list))
            query = "Choose an option number:"

            user_input = ui_service.get_input_valid_choice(valid_choices, query)

            if user_input.isdecimal():

                movie_id = movies_found[int(user_input)-1]['id']

    return movie_id
