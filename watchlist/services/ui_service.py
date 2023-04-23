from tabulate import tabulate
from ..services import ui_service


# options = list of lists (like rows in table)
# headers = list of strings
def print_options_table(headers, options):

    if options:

        table = []

        headers.insert(0, "")

        table.append(headers)

        for index, option in enumerate(options):

            row = []
            row.append(index+1)

            for key in option.keys():
                row.append(option[key])

            table.append(row)

        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', maxcolwidths=15, numalign="left", stralign="left" ))

    else:
        print_no_movies_found()

def get_valid_chosen_option_from_options(options, query, extra_choices=[]):

    valid_choices = list(map(lambda a : str(a), range(1, len(options)+1)))
    valid_choices.extend(extra_choices)
    user_input = get_input_valid_choice(valid_choices, query)

    return options[int(user_input)-1] if user_input.isdecimal() else user_input

def get_input_valid_choice(valid_choices, query):

    print(query)

    is_valid = False
    user_choice = None

    while not is_valid:
        user_choice = input()

        if is_valid_choice(user_choice, valid_choices):
            is_valid = True
        else:
            print("\nInvalid choice, please try again:")

    return user_choice

def is_valid_choice(choice, valid_choices):
    return choice in valid_choices

def confirm_choice(query):

    valid_choices = ['y', 'n', 'Y', 'N', 'yes', 'YES', 'no', 'NO']
    input = ui_service.get_input_valid_choice(valid_choices, query)

    return True if input in ['y', 'Y', 'YES', 'yes'] else False



def print_add_movie_summary(movie_title):
    print(f"\nThe movie {movie_title} was added to the database.\n")

def print_update_movie_summary(movie_title, is_watched):
    print(is_watched)
    status = '"Watched"' if is_watched else '"Not Watched"'
    print(f"\nThe movie {movie_title}'s watch status was updated to {status}.\n")

def print_delete_movie_summary(movie_title):
    print(f"\nThe movie {movie_title} was deleted from the database.\n")

def print_movie_was_not_deleted():
    print(f"\nThe movie was not deleted.\n")

def print_no_movies_found():
    print(f"\nNo movies were found.\n")