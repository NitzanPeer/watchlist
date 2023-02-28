# $ python -m unittest tests/test_tmdb.py -v

import unittest

from watchlist.services.movie_api.tmdb_api import TmdbAPI

class TestTMDBAPI(unittest.TestCase):

    def assert_search_results(self, movie_name, page_num):
        results = TmdbAPI.search(movie_name, page_num)
        self.assertIsInstance(results, list, "results should be a list")
        self.assertGreater(len(results), 0, "results should contain more than 0 elements")
        self.assertIsInstance(results[0], dict, "results element should be a dict")
        self.assertIn("id", results[0], "results[0] must contain the key 'id'")

    def assert_get_info(self, tmdb_id):
        info = TmdbAPI.get(tmdb_id)
        self.assertIsInstance(info, dict, "info should be a dict")
        self.assertGreater(len(info), 0, "info should contain more than 0 elements")
        self.assertIn("imdb_id", info, "info must contain the key 'imdb_id'")



    def test_search_titanic(self):
        movie_name = "Titanic"
        page_num = 1
        self.assert_search_results(movie_name, page_num)

    def test_search_the_matrix(self):
        movie_name = "The Matrix"
        page_num = 2
        self.assert_search_results(movie_name, page_num)

    def test_get_titanic_info(self):
        tmdb_id = 597
        self.assert_get_info(tmdb_id)

    def test_get_the_matrix_info(self):
        tmdb_id = 603
        self.assert_get_info(tmdb_id)



if __name__ == '__main__':
    unittest.main()