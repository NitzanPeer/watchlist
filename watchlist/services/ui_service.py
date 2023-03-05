from tabulate import tabulate


# options = list of dicts/lists (like rows in table)
# headers = list of strings
def print_options_table(headers, options):

    table = []

    headers.insert(0, "")

    table.append(headers)

    for index, option in enumerate(options):

        row = []
        row.append(index+1)

        for key in option.keys():
            row.append(option[key])

        table.append(row)

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

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

def print_add_movie_summary(movie_name):
    print(f"\nThe movie {movie_name} was added to the database.\n")

def print_update_movie_summary(movie_name, binary_status):
    print(binary_status)
    status = '"Watched"' if binary_status else '"Not Watched"'
    print(f"\nThe movie {movie_name}'s watch status was updated to {status}.\n")

def print_delete_movie_summary(movie_name):
    print(f"\nThe movie {movie_name} was deleted from the database.\n")

def print_movie_was_not_deleted():
    print(f"\nThe movie was not deleted.\n")




