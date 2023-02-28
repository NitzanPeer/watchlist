from ..services import exceptions
from .. import models
from ..services import movie_api
# should we put these in an init file and import it as a whole?:
from ..services import ui_service

# from watchlist.services.mysql_service import MySQLService
# mysql_service = MySQLService



# TODO: follow the planning of add as a guideline for this function, think of the controller as a recipe or instructions
# remember! every time you need to convert/change/manipulate data between functions, create here a function for it and call it from the "add" function

# Missing: validation, map()
# TODO: what's happening when you are trying to add an already existing movie?
def add(movie_name):

    try:
        chosen_tmdb_id = interactive_selection_menu(movie_name)
        movie_data = movie_api.get(chosen_tmdb_id)

        check_if_movie_already_exists_in_db(movie_data['imdb_id'])


        movie_id = add_movie_to_db(movie_data)
        watch_status = get_watch_status_from_user(movie_id)
        models.add_watch_status(movie_id, watch_status)
        ui_service.print_add_movie_summary(movie_name)




def add_movie_to_db(movie_data):

    # get movie
    # if not exist - create

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


def interactive_selection_menu(movie_name):



    query = "\nChoose an option number, 'n' for next page or 'p' for previous page:\n"
    page_num = 1
    no_choice_made = True

    while no_choice_made:

        response = movie_api.search(movie_name, page_num)
        # initialization happens needlessly each iteration but the line depends on response:

        page_results = response['results']
        total_num_of_pages = response['total_pages']

        if not total_num_of_pages:
            ui_service.print_no_movies_found_error()
            # TODO: throw custom exception to exit the application at the controller stage
            raise NoMoviesFoundError()


        print_worthy_list = []
        for result in page_results:
            print_worthy_list.append({'name': result['title'], 'year': result['release_date'][:4]})

        # get_five_results here (not working yet):
        # five_options = get_five_results()

        ui_service.print_options_table(["name", "year"], print_worthy_list)


        int_list = list(range(1, len(page_results)+1))
        valid_choices = list(map(lambda a : str(a), int_list))

        if page_num == total_num_of_pages:
            valid_choices.append('p')

        elif page_num == 1:
            valid_choices.append('n')

        else:
            valid_choices.extend(['n', 'p'])

        user_input = ui_service.get_input_valid_choice(valid_choices, query)


        if user_input.isdecimal():

            movie_id = page_results[int(user_input)-1]['id']
            no_choice_made = False

        elif user_input == 'n':
            page_num += 1

        elif user_input == 'p':
            page_num -= 1

    print(movie_id)
    return movie_id


# this func doesn't include progression:
def get_five_results(page_results, starting_point):
    five_results = []

    for index, result in enumerate(page_results):
        if index < 5:
            five_results.append(result)

    for result in page_results[starting_point:]:
        five_results.append(result)


def get_watch_status_from_user(movie_id):

    query = "Did you watch this movie? ('y' for yes, 'n' for no)"
    valid_choices = ['y', 'n', 'Y', 'N']
    input = ui_service.get_input_valid_choice(valid_choices, query)

    if input == 'y' or input == 'Y':
        models.mark_as_watched(movie_id)
        result = 1
    if input == 'n' or input == 'N':
        models.mark_as_unwatched(movie_id)
        result = 0

    return result


def check_if_movie_already_exists_in_db(imdb_id):
    if models.find_movie_by_imdb_id(imdb_id):
        # print_movie_already_exists_error(movie_name)
        movie_name = 'tttest'
        raise exceptions.MovieAlreadyExistsError(f"The movie {movie_name} already exist you bastard.")



# initial error fixed (status marking funcs returned nothing instead of 0 or 1)
# check_if_movie_exists_in_db added