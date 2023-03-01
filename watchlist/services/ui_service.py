from tabulate import tabulate

#undeeded?
def print_no_movies_found_error(movie_name):
    print(f"No movie named {movie_name} was found.")

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


# you can use map() to create a list of stringed ints
def get_input_valid_choice(valid_choices, query):

    # valid_choices will be produced somewhere else (controller?) as a list that will contain 'n','p' and
    # a range of STRINGED INTS! (probably range(:total_page_results))
    # that will be created using the built-in map() func
    # validation will be handled there as well

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

