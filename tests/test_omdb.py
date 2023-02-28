# $ python -m unittest tests/test_omdb.py -v

import unittest


from watchlist.services.movie_api.omdb_api import OmdbAPI

class TestOMDBRatings(unittest.TestCase):

    demo_ratings = [
        {'Source': 'Internet Movie Database', 'Value': '8.7/10'},
        {'Source': 'Rotten Tomatoes', 'Value': '88%'},
        {'Source': 'Metacritic', 'Value': '73/100'}
    ]


    def assert_get_info(self, imdb_id):
        info = OmdbAPI.get(imdb_id)
        self.assertIsInstance(info, dict, "info should be a dict")
        self.assertGreater(len(info), 0, "info should contain more than 0 elements")
        self.assertIn("imdbRating", info, "info must contain the key 'imdbRating'")


    def test_get_the_matrix_info(self):
        imdb_id = "tt0133093"
        self.assert_get_info(imdb_id)


    def test_rt_rating_should_return_88(self):
        result = OmdbAPI.get_rt_rating(self.demo_ratings)
        self.assertEqual(result, 88, "Should return 88")

    def test_rt_rating_should_return_None(self):
        result = OmdbAPI.get_rt_rating([])
        self.assertIsNone(result, "Should return None")



if __name__ == '__main__':
    unittest.main()