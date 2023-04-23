import urllib.parse
import requests


class TmdbAPI:
    api_key = 'b5b1baac3d56cc9ee08b4e017486795d'
    base_url = 'https://api.themoviedb.org/3/'


    # need to check if only one result
    @staticmethod
    def get_user_picked_movie_id(all_results_list):

        if len(all_results_list) == 1:
            return all_results_list[0]["id"]

        start = 0
        end = 5

        five_results_max = []
        user_input = 'NEXT'

        while user_input == 'NEXT':

            for dict in all_results_list[start:end]:
                five_results_max.append(
                    {
                        "title": dict["title"],
                        "year": dict["release_date"][:4],
                        "id": dict["id"]
                    }
                )
            print(five_results_max)

            user_input = input(f'\nenter the wanted movie\'s id or "NEXT" to continue\n')
            if user_input == 'NEXT':
                start += 5
                end += 5
            else:
                return user_input


    @staticmethod
    def search(movie_title, page_num):
        # https://api.themoviedb.org/3/search/movie?api_key=b5b1baac3d56cc9ee08b4e017486795d&language=en-US&query=Titanic&page=1&include_adult=false

        encoded_name = urllib.parse.quote(movie_title)
        specific_api = f"{TmdbAPI.base_url}search/movie?api_key={TmdbAPI.api_key}&language=en-US&query={encoded_name}&page={page_num}&include_adult=false"
        response = requests.get(specific_api)
        response_json = response.json()

        return response_json



    @staticmethod
    def get(tmdb_id):
        # https://api.themoviedb.org/3/movie/597?api_key=b5b1baac3d56cc9ee08b4e017486795d&language=en-US

        specific_api = f"{TmdbAPI.base_url}/movie/{tmdb_id}?api_key={TmdbAPI.api_key}"
        response = requests.get(specific_api)

        return response.json()



