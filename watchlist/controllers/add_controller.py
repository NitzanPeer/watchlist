from ..services import exceptions
from .. import models
from ..services import movie_api
from ..services import ui_service
from ..services import util


def add(movie_name):

    chosen_tmdb_id = interactive_selection_menu(movie_name)
    movie_data = movie_api.get(chosen_tmdb_id)
    movie_id = add_movie_to_db(movie_data)
    watch_status = util.get_watch_status_from_user(movie_id)
    models.add_watch_status(movie_id, watch_status)
    ui_service.print_add_movie_summary(movie_name)

def interactive_selection_menu(movie_name):

    page_num = 1
    no_choice_made = True

    while no_choice_made:

        response = movie_api.search(movie_name, page_num)

        page_results = response['results']
        total_num_of_pages = response['total_pages']

        if not page_results:
            raise exceptions.NoMoviesFoundError(f"No movies named {movie_name} were found.")

        # repeats, move to util:
        print_worthy_list = []
        for result in page_results:
            print_worthy_list.append({'name': result['title'], 'year': result['release_date'][:4]})

        ui_service.print_options_table(["name", "year"], print_worthy_list)

        # repeats, move to util:
        int_list = list(range(1, len(page_results)+1))
        valid_choices = list(map(lambda a : str(a), int_list))

        if page_num == total_num_of_pages:
            valid_choices.append('p')
            query = "\nChoose an option number or 'p' for previous page:\n"

        elif page_num == 1:
            valid_choices.append('n')
            query = "\nChoose an option number or 'n' for next page:\n"

        else:
            valid_choices.extend(['n', 'p'])
            query = "\nChoose an option number, 'n' for next page or 'p' for previous page:\n"

        user_input = ui_service.get_input_valid_choice(valid_choices, query)


        if user_input.isdecimal():

            movie_id = page_results[int(user_input)-1]['id']
            no_choice_made = False

        elif user_input == 'n':
            page_num += 1

        elif user_input == 'p':
            page_num -= 1

    return movie_id

def add_movie_to_db(movie_data):

    if is_movie_exists(movie_data['imdb_id']):
        raise exceptions.MovieAlreadyExistsError(f"\nThe movie {movie_data['name']} already exists.")

    movie_id = models.add_movie(
        name=movie_data['name'],
        year=movie_data['year'],
        director=movie_data['director'],
        genres=movie_data['genres'],
        imdb_id=movie_data['imdb_id'],
        imdb_score=movie_data['imdb_score'],
        rotten_tomatoes_score=movie_data['rotten_tomatoes_score'],
        description=movie_data['description'],
    )

    return movie_id

# this func doesn't include progression:
def get_five_results(page_results, starting_point):
    five_results = []

    for index, result in enumerate(page_results):
        if index < 5:
            five_results.append(result)

    for result in page_results[starting_point:]:
        five_results.append(result)

def is_movie_exists(imdb_id):
    return bool(models.find_movie_by_imdb_id(imdb_id))




#TODO:
# validation (raise exception for null values in non-null columnns)
# map()?

# when trying to insert Titanic option 4 it throws "Unknown column 'None' in 'field list'" error
    # 1. why is it talking about the column if the "None" is a column value?
    # 2. how do we turn None values into null so mysql will accept it?

