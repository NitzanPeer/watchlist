# $ python -m unittest tests/mini_tests -v

import requests
from watchlist.services.mysql_service import MySQLService
import mysql.connector
from watchlist.services.ui_service import print_options_table, print_no_movies_found_error, print_add_movie_summary, get_input_valid_choice

from __convert_python_value_to_sql import *

mysql_service = MySQLService()

table_name = "movies"



# demo_key_value_data = \
#     {
#         'title': 'Titanic',
#         'year': 1998,
#         'imdb_score': 79,
#         'imdb_id': 200,
#     }

# demo_where_data = \
#     [
#         {
#             'column': 'year',
#             'operator': '>',
#             'value': 1998
#         },
#         {
#             'column': 'imdb_score',
#             'operator': '>=',
#             'value': 70
#         }
#     ]

# demo_limit = \
#     {
#         'offset': 1,
#         'count': 2
#     }

# demo_order_by_columns = \
#     [
#         {
#             'column': 'id',
#             'order': 'DESC'
#         },
#         {
#             'column': 'title',
#         }
#     ]

# demo_columns = ['id', 'title']


# page_results = [
#     {
#       "backdrop_path": "/rzdPqYx7Um4FUZeD8wpXqjAUcEm.jpg",
#       "genre_ids": [
#         18,
#         10749
#       ],
#       "id": 597,
#       "original_language": "en",
#       "original_title": "Titanic",
#       "overview": "101-year-old Rose DeWitt Bukater tells the story of her life aboard the Titanic, 84 years later. A young Rose boards the ship with her mother and fiancé. Meanwhile, Jack Dawson and Fabrizio De Rossi win third-class tickets aboard the ship. Rose tells the whole story from Titanic's departure through to its death—on its first and last voyage—on April 15, 1912.",
#       "popularity": 319.114,
#       "poster_path": "/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
#       "release_date": "1997-11-18",
#       "title": "Titanic",
#       "vote_average": 7.888,
#       "vote_count": 22350
#     },
#     {
#       "backdrop_path": "/edHgXEtPbyVIQ7xKb1cvJJqTVhA.jpg",
#       "genre_ids": [
#         28,
#         18,
#         36
#       ],
#       "id": 11021,
#       "original_language": "de",
#       "original_title": "Titanic",
#       "overview": "This little-known German film retells the true story of the British ocean liner that met a tragic fate. Ernst Fritz Fürbringer plays the president of the White Star Line, who unwisely pressed the Titanic's captain (Otto Wernicke) to make the swiftest possible crossing to New York.",
#       "popularity": 21.797,
#       "poster_path": "/Al7oIXQ4dZAofBTZWm6OiXS3MEa.jpg",
#       "release_date": "1943-11-10",
#       "title": "Titanic",
#       "vote_average": 6.1,
#       "vote_count": 51
#     }
# ]



# options = \
#     [
#         {
#             'index': '1',
#             'title': 'Titanic',
#             'year': '1997'
#         },
#         {
#             'index': '2',
#             'title': 'Titanic',
#             'year': '1943'
#         }
#     ]

# headers = ['', 'title', 'Year']






# print_options_table(headers, options)

# query = f"\nPlease enter a number of movie, 'n' for next page or 'p' for previous page"
# print(get_input_valid_choice(['n', 'p', '1','2','3'], query))


# var3 = 'x'

# def foo(var3):
#     var2 = []
#     bar(var2)
#     print(var2)

#     bar1(var3)
#     print(var3)

# def bar(var2):
#     var2.append("a")

# def bar1(var3):
#     var3 = var3 + "a"

# foo(var3)

# def foo2(var3):
#     var3 += "a"
#     print(var3)



# print(print_options_table('titanic'))
# sug_shel_main('titanic')



# print(mysql_service.select_all(table_name, columns=[], where_data=None, order_by_columns=demo_order_by_columns, limit=demo_limit))
# print(mysql_service.select_one(table_name, columns=demo_columns, where_data=demo_where_data, order_by_columns=demo_order_by_columns))
# print(mysql_service.select_one(table_name, columns=[], where_data=None, order_by_columns=[]))


# not a ui flow, most of it's logic should reside in the controller
# def sug_shel_ui(movie_name):

#     query = "\nChoose an option number, 'n' for next page or 'p' for previous page:\n"
#     page_num = 1
#     no_choice_made = True

#     while no_choice_made:

#         response = TmdbAPI.search(movie_name, page_num)
#         print_options_table(movie_name, page_num, response)
#         page_results = response['results']
#         # initialization happens each itteration needlessly but the line depends on response:
#         total_num_of_pages = response['total_pages']

#         # implementation needed:
#         # user_input = get_input_valid_choice(['n', 'p', range(index)], query)

#         user_input = input(query)

#         if user_input.isdecimal() and int(user_input) in range(index):

#             movie_id = page_results[int(user_input)-1]['id']
#             no_choice_made = False

#         elif user_input == 'n' and page_num != total_num_of_pages:
#             page_num += 1

#         elif user_input == 'p' and page_num != 1:
#             page_num -= 1

#         else:
#             print("\nInvalid Choice, please try again:\n")
#             index -= 1


#     print_add_movie_summary(movie_name)
#     return movie_id

   # nagla0 = 0 - 5
    # nagla1 = 5 - 10
    # nagla2 = 10 - 15

    # @staticmethod
    # def get_five_results(all_results):
    #     i = 0
    #     step = 5
    #     five_results_max = []
    #     for i in range(len(all_results)):
    #         print(range(len(all_results)))
    #         if i==0:
    #             end_index = (step * i) + 5
    #             five_results_max.append(all_results[0:end_index])
    #         else:
    #             start_index = step * i
    #             end_index = (step * i) + 5
    #             five_results_max.append(all_results[start_index:end_index])

    #     return five_results_max


# used to be part of print_options_table:

    # total_num_of_pages = response['total_pages']
    # response = TmdbAPI.search(movie_name, page_num)
    # page_results = response['results']

    # for result in page_results:
    #     table.append([index, result['title'], result['release_date'][:4]])
    #     index += 1

    # print(f"\nPage {page_num} out of {total_num_of_pages}\n")






# def dict_to_key_list(dictionary):
#     return ', '.join(list(dictionary.keys()))


# def dict_to_value_list(dictionary):
#     value_list = f"{list(dictionary.values())}"
#     return value_list[1:-1]

# def where_clause_handling(where_data):
#     where_clause = ""
#     for dictionary in where_data:

#         column = f"{dictionary['column']} "
#         operator = f"{dictionary['operator']} "

#         if isinstance(dictionary['value'], str):
#             value = f"'{dictionary['value']}'"
#         else:
#             value = f"{dictionary['value']}"

#         where_clause += column + operator + value
#         where_clause += " AND "


#     return f"WHERE {where_clause[:-5]}"


# def set_clause_handling(set_data):

#     set_clause = ""

#     for key in set_data:
#         if type(set_data[key]) == str:
#             set_clause += f"{key} = '{set_data[key]}'"
#         else:
#             set_clause += f"{key} = {set_data[key]}"
#         set_clause += ", "

#     return set_clause[:-2]

# def insert(table, insert_data):

#     key_list = dict_to_key_list(insert_data)
#     value_list = dict_to_value_list(insert_data)

#     print(f"INSERT INTO {table} ({key_list}) VALUES ({value_list});")


# def update(table, set_data, where_data=None):

#     set_clause = set_clause_handling(set_data)

#     update_set_clause = f"UPDATE {table} SET {set_clause}"

#     if not where_data:
#         print(f"{update_set_clause};")

#     else:
#         where_clause = where_clause_handling(where_data)
#         print(f"{update_set_clause} {where_clause};")


# def delete(table, where_data=None):

#     delete_from_clause = f"DELETE FROM {table}"

#     if not where_data:
#         print(f"{delete_from_clause};")

#     else:
#         where_clause = where_clause_handling(where_data)
#         print(f"{delete_from_clause} {where_clause};")


# def select(table, columns=[], where_data=None):

#     columns_as_string = ", ".join(columns) if columns else '*'

#     select_from_clause = f"SELECT {columns_as_string} FROM {table}"

#     if not where_data:
#         raw_query(f"{select_from_clause};", False)

#     else:
#         where_clause = where_clause_handling(where_data)
#         raw_query(f"{select_from_clause} {where_clause};", False)


# def raw_query(self, query, is_commit=True):
#     result = self.cursor.execute(query)
#     if is_commit:
#         self.connection.commit()

#     return result



# select("movies")
# select("movies", where_data=demo_where_data)
# select("movies", "imdb_score", demo_where_data)
# need to make work (change default):
# select("movies", ["imdb_score", "name"], None)

# insert("movies", demo_key_value_data)


# update("movies", demo_key_value_data, demo_where_data)
# update("movies", demo_key_value_data)

# delete("movies", demo_where_data)

quit()















# list1 = [1, 2, 3,4,5,6,7]
# dict1 = {"key1": 1, "key2": 2, "key3": 3}

# num1, num2, *num3 = list1

# print(num1)
# print(num2)
# print(num3)

# print(list1)
# print("----------")
# print(*list1)
# print(type(*list1))
# print("----------")
# print(dict1)
# print("----------")
# print(*dict1)
# print("----------")
# print(**dict1)




movie_name = "Titanic"


demo_ratings = [
    {'Source': 'Internet Movie Database', 'Value': '8.7/10'},
    {'Source': 'Rotten Tomatoes', 'Value': '88%'},
    {'Source': 'Metacritic', 'Value': '73/100'}
]


rating_sources = []
for rating in demo_ratings:
        rating_sources.append(rating['Source'])

print(", ".join(rating_sources))


quit()


# test for finding RT rating without specifying location:"

omdb_api = 'http://www.omdbapi.com/?i=tt0133093&apikey=80fafa3a'
tmdb_api = 'https://api.themoviedb.org/3/movie/550?api_key=b5b1baac3d56cc9ee08b4e017486795d'
response_omdb = requests.get(omdb_api)
response_tmdb = requests.get(tmdb_api)
omdb_json = response_omdb.json()
tmdb_json = response_tmdb.json()


def get_rt_rating(ratings):
    rt_rating = None
    for rating in ratings:
        if rating['Source'] == "Rotten Tomatoes":
            rt_rating = rating['Value'][:-1]

    return rt_rating

get_rt_rating(omdb_json['Ratings'])


# ----------------------------------------------------


modified_name = movie_name.replace(" ", "+")
specific_api = f"https://api.themoviedb.org/3/search/movie?api_key=b5b1baac3d56cc9ee08b4e017486795d&language=en-US&query={modified_name}&page=1&include_adult=false"
response = requests.get(specific_api)
response_json = response.json()
all_results_list = response_json["results"]
# print(response_json["results"][0]["id"])
# print(response_json["results"][0]["title"])
# print(response_json["results"][0]["release_date"][:4])


# test for getting 5 results:

def get_five_results(start, end):
    new_list_of_dicts = []
    for dict in all_results_list[start:end]:
        new_list_of_dicts.append(
            {
                "title": dict["title"],
                "year": dict["release_date"][:4],
                "id": dict["id"]
            }
        )


    return new_list_of_dicts

    # print(new_list_of_dicts)


start = 0
end = 5

print(get_five_results(start, end))

user_input = input("\nEnter the wanted movie's id or type 'next' to see more options:\n")
if user_input == "next":
    # check if there are more options left and if so - how many?
    start += 5
    end += 5


# -----------------------------------------





# why didn't this work?
# index = 0
# new_list_of_dicts = []
# while index < 5:

#     for dict in all_results_list:
#         new_list_of_dicts.append(
#             {
#             "title": response_json["results"][index]["title"],
#             "year": response_json["results"][index]["release_date"][:4]
#             }
#         )
#         index += 1
#         print(index)




