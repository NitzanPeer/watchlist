from ..services import exceptions
from .. import models
from ..services import ui_service
from ..services import util



def update(movie_name):


    movie_id = interactive_selection_menu(movie_name)
    query = "Did you watch this movie? ('y' for yes, 'n' for no)"
    watch_status = ui_service.confirm_choice(query)
    models.update_watch_status(movie_id, watch_status)

    ui_service.print_update_movie_summary(movie_name, watch_status)


def interactive_selection_menu(movie_name):

    # validation? what if not a list?

    movies_found = models.find_movie_by_name(movie_name)

    if not movies_found:
        raise exceptions.NoMoviesFoundError(f"No movies named {movie_name} were found.")

    # repeats, move to util
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

            # repeats, move to util:
            int_list = list(range(1, len(movies_found)+1))
            valid_choices = list(map(lambda a : str(a), int_list))

            query = "Choose an option number:"
            user_input = ui_service.get_input_valid_choice(valid_choices, query)
            movie_id = movies_found[int(user_input)-1]['id']

    return movie_id



# TODO:


# DONE:
# __find_movie_by_column was changed from select_one to select_all
# added print_update_movie_summary and print_delete_movie_summary
# get_watch_status_from_user moved to util
# added is_watched condition to update_watch_status
# trying to fix get_watch_status_by_movie_id