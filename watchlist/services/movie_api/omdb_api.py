import requests


class OmdbAPI:
    api_key = '80fafa3a'

    @staticmethod
    def get(imdb_id):
        # https://www.omdbapi.com/?i=tt0133093&apikey=80fafa3a

        specific_api = f"https://www.omdbapi.com/?i={imdb_id}&apikey=80fafa3a"
        response = requests.get(specific_api)

        return response.json()

    @staticmethod
    def get_rt_rating(ratings):
        rt_rating = None
        for rating in ratings:
            if rating['Source'] == "Rotten Tomatoes":
                rt_rating = int(rating['Value'][:-1])


        return rt_rating
