# $ python -m unittest tests/test_ui_service.py -v

import unittest

from watchlist.services.ui_service import is_valid_choice

from watchlist.services.mysql_service import MySQLService

mysql_service = MySQLService()

demo_choice = "?"
demo_is_not_valid = "?"
demo_is_valid = "?"

class Test_UISERVICE(unittest.TestCase):

    def assert_is_valid_choice_result(self, choice, valid_choices):
        result = is_valid_choice(choice, valid_choices)
        self.assertTrue()
        self.assertIn()
        self.assertNotIn()


    def assert_select_all_results(self, table_name, columns=[], where_data=None, order_by_columns=[], limit={}):
        results = mysql_service.select_all(table_name, columns, where_data, order_by_columns, limit)
        self.assertIsInstance(results, list, "results should be a list")
        if results:
            self.assertIsInstance(results[0], dict, "results element should be a dict")
            self.assertIn("id", results[0], "results[0] must contain the key 'id'")




    def test_is_valid_choice_valid(self):
        self.assert_insert_result(table_name='movies', insert_data=self.demo_insert)

    def test_is_valid_choice_invalid(self):
        pass



if __name__ == '__main__':
    unittest.main()