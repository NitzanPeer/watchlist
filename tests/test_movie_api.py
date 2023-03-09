# $ python -m unittest tests/test_movie_api.py -v

import unittest

from watchlist.services import movie_api


class TestMovieAPI(unittest.TestCase):

    demo_genres = [
        {
         "id": 18, "title": "Drama"
        },
        {
        "id": 10749, "title": "Romance"
        }
    ]

    def assert_search_results(self, movie_title):
        results = movie_api.search(movie_title)
        self.assertIsInstance(results, list, "results should be a list")
        self.assertGreater(len(results), 0, "results should contain more than 0 elements")
        self.assertIsInstance(results[0], dict, "results element should be a dict")
        self.assertIn("id", results[0], "results[0] must contain the key 'id'")


    def assert_get_info(self, tmdb_id):
        info = movie_api.get(tmdb_id)
        self.assertIsInstance(info, dict, "info should be a dict")
        self.assertGreater(len(info), 0, "info should contain more than 0 elements")
        self.assertIn("imdb_score", info, "info must contain the key 'imdb_score'")


    def test_search_titanic(self):
        movie_title = "Titanic"
        self.assert_search_results(movie_title)

    def test_search_the_matrix(self):
        movie_title = "The Matrix"
        self.assert_search_results(movie_title)

    def test_get_titanic_info(self):
        tmdb_id = 597
        self.assert_get_info(tmdb_id)

    def test_get_the_matrix_info(self):
        tmdb_id = 603
        self.assert_get_info(tmdb_id)



    def test_get_the_avatar2_info(self):
        tmdb_id = 76600
        info = movie_api.get(tmdb_id)

        # data = {'title': 'Avatar: The Way of Water', 'director': 'James Cameron', 'genres': 'Science Fiction, Adventure, Action', 'year': '2022', 'description': 'Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.', 'imdb_id': 'tt1630029', 'imdb_score': '7.9', 'rotten_tomatoes_score': 77}

        scheme = {
            'title': str,
            'director': str,
            'genres': str,
            'year': str,
            'description': str,
            'imdb_id': str,
            'imdb_score': float,
            'rotten_tomatoes_score': int,
        }

        for key in scheme:
            self.assertIn(key, info)
            # self.assertIsInstance(info[key], scheme[key])
            self.assertIsInstance(info.get(key), scheme[key])



        # self.assertEqual(info, data)




    def test_get_genres_as_string(self):
        result = movie_api.get_genres_as_string(self.demo_genres)
        self.assertIsInstance(result, str, "result should be a string")



if __name__ == '__main__':
    unittest.main()
