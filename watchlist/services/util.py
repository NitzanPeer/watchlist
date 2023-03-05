from .. import models
from ..services import ui_service


def get_watch_status_from_user(movie_id):

    query = "Did you watch this movie? ('y' for yes, 'n' for no)"
    valid_choices = ['y', 'n', 'Y', 'N']
    input = ui_service.get_input_valid_choice(valid_choices, query)

    # could be one line:
    if input in ['y', 'Y']:
        models.mark_as_watched(movie_id)
        result = True
    else:
        models.mark_as_unwatched(movie_id)
        result = False

    return result



# add_controller
################

# repeats, move to util:
print_worthy_list = []
for result in page_results:
    print_worthy_list.append({'name': result['title'], 'year': result['release_date'][:4]})

ui_service.print_options_table(["name", "year"], print_worthy_list)

# repeats, move to util:
int_list = list(range(1, len(page_results)+1))
valid_choices = list(map(lambda a : str(a), int_list))




# update_controller
###################

# repeats, move to util:
print_worthy_list = []
for movie in movies_found:
    print_worthy_list.append({'name': movie['name'], 'year': movie['year']})

ui_service.print_options_table(["name", "year"], print_worthy_list)


# repeats, move to util:
int_list = list(range(1, len(movies_found)+1))
valid_choices = list(map(lambda a : str(a), int_list))
query = "Choose an option number:"

user_input = ui_service.get_input_valid_choice(valid_choices, query)

if user_input.isdecimal():

    movie_id = movies_found[int(user_input)-1]['id']

# repeats, move to util
valid_choices = ['y', 'n', 'Y', 'N']
query = "Is this the movie you were looking for? (enter 'y' for YES or 'n' for NO)"
user_input = ui_service.get_input_valid_choice(valid_choices, query)




# delete_controller
###################


# repeated, move to util:
int_list = list(range(1, len(movies_found)+1))
valid_choices = list(map(lambda a : str(a), int_list))
query = "Choose an option number:"

user_input = ui_service.get_input_valid_choice(valid_choices, query)

if user_input.isdecimal():

    movie_id = movies_found[int(user_input)-1]['id']




