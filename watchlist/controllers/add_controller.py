from ..services import exceptions
from .. import models
from ..services import movie_api
from ..services import ui_service
from ..services import util


def add(movie_title):

    chosen_tmdb_id = interactive_selection_menu(movie_title)
    movie_data = movie_api.get(chosen_tmdb_id)
    movie_id = add_movie_to_db(movie_data)

    query = "Did you watch this movie? ('y' for yes, 'n' for no)"
    models.add_watch_status(movie_id, ui_service.confirm_choice(query))

    ui_service.print_add_movie_summary(movie_title)

def interactive_selection_menu(movie_title):

    page_num = 1
    no_choice_made = True

    while no_choice_made:

        response = movie_api.search(movie_title, page_num)

        page_results = response['results']
        total_num_of_pages = response['total_pages']

        if not page_results:
            raise exceptions.NoMoviesFoundError(f"No movies named {movie_title} were found.")

        extracted_data = util.extract_title_and_year(page_results)
        ui_service.print_options_table(["title", "year"], extracted_data)

        extra_choices = []

        if total_num_of_pages == 1:
            query = "\nChoose an option number:\n"

        elif page_num == total_num_of_pages:
            extra_choices.append('p')
            query = "\nChoose an option number or 'p' for previous page:\n"

        elif page_num == 1:
            extra_choices.append('n')
            query = "\nChoose an option number or 'n' for next page:\n"

        else:
            extra_choices.extend(['n', 'p'])
            query = "\nChoose an option number, 'n' for next page or 'p' for previous page:\n"


        result = ui_service.get_valid_chosen_option_from_options(page_results, query, extra_choices)

        if result == 'n':
            page_num += 1

        elif result == 'p':
            page_num -= 1

        else:
            movie_id = result['id']
            no_choice_made = False

    return movie_id

def add_movie_to_db(movie_data):

    if is_movie_exists(movie_data['imdb_id']):
        raise exceptions.MovieAlreadyExistsError(f"\nThe movie {movie_data['title']} already exists.")

    movie_id = models.add_movie(
        title=movie_data['title'],
        year=movie_data['year'],
        director=movie_data['director'],
        genres=movie_data['genres'],
        imdb_id=movie_data['imdb_id'],
        imdb_score=movie_data['imdb_score'],
        rotten_tomatoes_score=movie_data['rotten_tomatoes_score'],
        description=movie_data['description'],
    )

    return movie_id


def is_movie_exists(imdb_id):
    return bool(models.find_movie_by_imdb_id(imdb_id))

# TODO: how do we display 5 results instead of a full page?
def get_five_results(page_results, starting_point):
    five_results = []

    for index, result in enumerate(page_results):
        if index < 5:
            five_results.append(result)

    for result in page_results[starting_point:]:
        five_results.append(result)



