# $ python -m unittest tests/test_mysql_service.py -v

import unittest

from watchlist.services.mysql_service import MySQLService

# mysql_service = MySQLService()


class Test_MYSQLSERVICE(unittest.TestCase):

    mysql_service = None

    demo_table_name = 'test'

    demo_create_db_query = \
        f"""
        CREATE DATABASE IF NOT EXISTS test;
        """

    demo_use_db_query = \
        f"""
        USE test;
        """

    demo_create_table_query = \
    f"""
        CREATE TABLE IF NOT EXISTS {demo_table_name} (
            id INT NOT NULL AUTO_INCREMENT,
            title VARCHAR(50) NOT NULL,
            director VARCHAR(50),
            genres VARCHAR(50),
            year YEAR,
            description TEXT,
            imdb_id VARCHAR(11),
            imdb_score FLOAT(3),
            rotten_tomatoes_score INT,
            PRIMARY KEY(id)
        );
    """

    demo_columns = ['id', 'title']

    demo_order_by_columns = [
        {
            'column': 'id',
            'order': 'DESC'
        },
        {
            'column': 'title',
        }
    ]

    demo_limit = {
        'offset': 3,
        'count': 2
    }

    demo_where = [
        {
            'column': 'title',
            'operator': '=',
            'value': 'test1'
        },
        {
            'column': 'imdb_score',
            'operator': '<=',
            'value': 11
        }
    ]


    demo_false_where = [
        {
            'column': 'title',
            'operator': '=',
            'value': 'non_exist'
        }
    ]

    demo_where_all_columns = [
        {
            'column': 'imdb_score',
            'operator': '<=',
            'value': 3.3
        }
    ]

    demo_insert = {
        'title': 'TEST',
        'year': 1998,
        'imdb_score': 79,
        'imdb_id': 200
    }

    demo_set = {
        'title': 'TEST',
        'year': 1998,
        'imdb_score': 85,
        'imdb_id': 305
    }

    @classmethod
    def setUpClass(cls):
        cls.mysql_service = MySQLService()
        cls.mysql_service.raw_query(cls.demo_create_db_query)
        cls.mysql_service.raw_query(cls.demo_use_db_query)
        cls.mysql_service.raw_query(cls.demo_create_table_query)

    @classmethod
    def tearDownClass(cls):
        cls.mysql_service.raw_query(f"DROP TABLE {cls.demo_table_name};")
        cls.mysql_service.disconnect()


    def setUp(self):
        self.mysql_service.raw_query(f"""
            INSERT INTO {self.demo_table_name}
            (id, title, director, genres, year, description, imdb_id, imdb_score, rotten_tomatoes_score)
            VALUES
            (1, 'test1', 'director_test1', 'genres_test1', 1981, 'description_test1', 1, 1.1, 11),
            (2, 'test2', 'director_test2', 'genres_test2', 1982, 'description_test2', 2, 2.2, 22),
            (3, 'test3', 'director_test3', 'genres_test3', 1983, 'description_test3', 3, 3.3, 33)
        """)
        return super().setUp()

    def tearDown(self):
        self.mysql_service.raw_query(f"TRUNCATE TABLE {self.demo_table_name};")
        return super().tearDown()



    def assert_select_all_results(self, table_name, columns=[], where_data=None, order_by_columns=[], limit={}):
        results = self.mysql_service.select_all(table_name, columns, where_data, order_by_columns, limit)
        self.assertIsInstance(results, list, "results should be a list")
        if results:
            self.assertIsInstance(results[0], dict, "results element should be a dict")
            self.assertIn("id", results[0], "results[0] must contain the key 'id'")

    def assert_select_one_result(self, table_name, columns=[], where_data=None, order_by_columns=[]):
        result = self.mysql_service.select_one(table_name, columns, where_data, order_by_columns)
        self.assertIsInstance(result, dict, "result should be a dict")

    # def assert_insert_result(self, table_name, insert_data):
    #     result = self.mysql_service.insert(table_name, insert_data)
    #     self.assertIsInstance(result, int, "result should be an int")
    #     self.assertIsNotNone(result)

    def assert_update_result(self, table_name, set_data, where_data=None):
        result = self.mysql_service.update(table_name, set_data, where_data)
        self.assertIsInstance(result, int, "result should be an int")
        self.assertIsNotNone(result)

    def assert_delete_result(self, table_name, where_data):
        result = self.mysql_service.delete(table_name, where_data)
        self.assertEqual(result, 1, "one row should be deleted")
        self.assertIsNotNone(result)



    def test_insert_result(self):
        # self.assert_insert_result(table_name=self.demo_table_name, insert_data=self.demo_insert)
        result = self.mysql_service.insert(self.demo_table_name, self.demo_insert)
        self.assertIsInstance(result, int, "result should be an int")
        self.assertIsNotNone(result)

    def test_select_all_nones(self):
        # self.assert_select_all_results(table_name=self.demo_table_name, columns=[], where_data=None, order_by_columns=[], limit={})
        results = self.mysql_service.select_all(self.demo_table_name, [], None, [], {})
        self.assertIsInstance(results, list, "results should be a list")

        self.assertGreaterEqual(len(results), 1)
        self.assertIsInstance(results[0], dict, "results element should be a dict")
        self.assertIn("id", results[0], "results[0] must contain the key 'id'")

    def test_select_all_full_parameters(self):
        # self.assert_select_all_results(
        #     table_name=self.demo_table_name,
        #     columns=self.demo_columns,
        #     where_data=self.demo_where,
        #     order_by_columns=self.demo_order_by_columns,
        #     limit=self.demo_limit
        # )

        results = self.mysql_service.select_all(
            self.demo_table_name,
            self.demo_columns,
            self.demo_where_all_columns,
            self.demo_order_by_columns,
            # self.demo_limit
        )
        self.assertIsInstance(results, list, "results should be a list")

        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], dict, "results element should be a dict")
        self.assertIn("id", results[0], "results[0] must contain the key 'id'")

        self.assertEqual(len(results[0].keys()), 2)


    def test_select_one_nones(self):
        self.assert_select_one_result(table_name=self.demo_table_name, columns=[], where_data=None, order_by_columns=[])

    def test_select_one_full_parameters(self):
        self.assert_select_one_result(
            table_name=self.demo_table_name,
            columns=self.demo_columns,
            where_data=self.demo_where,
            order_by_columns=self.demo_order_by_columns)

    def test_update(self):
        self.assert_update_result(table_name=self.demo_table_name, set_data=self.demo_set, where_data=self.demo_where)


    # test that delete actually deletes:
        # 1. the return value matches the expected return value (DONE)
        # 2. if the table doesn't have what was deleted (DONE)
    def test_delete_one_row(self):
        delete_result = self.mysql_service.delete(self.demo_table_name, self.demo_where)
        self.assertEqual(delete_result, 1, "one row should be deleted")
        self.assertIsNotNone(delete_result)

        select_result = self.mysql_service.select_one(
            self.demo_table_name,
            columns=self.demo_columns,
            where_data=self.demo_where,
            order_by_columns=[])
        self.assertIsNone(select_result)

    def test_delete_no_rows(self):
        where = [
            {
                'column': 'title',
                'operator': '=',
                'value': 'non_exist'
            }
        ]
        delete_result = self.mysql_service.delete(self.demo_table_name, where)

        self.assertEqual(delete_result, 0, "no rows should be deleted")

        select_result = self.mysql_service.select_one(
            self.demo_table_name,
            columns=self.demo_columns,
            where_data=self.demo_where,
            order_by_columns=[])

        self.assertIsInstance(select_result, dict, "result should be a dict")

    def test_delete_all_rows(self):
        delete_result = self.mysql_service.delete(self.demo_table_name, self.demo_where_all_columns)

        self.assertEqual(delete_result, 3, "all rows should be deleted")
        self.assertIsInstance(delete_result, int, "result should be numeric")

        select_result = self.mysql_service.select_all(
            self.demo_table_name,
            columns=self.demo_columns,
            where_data=self.demo_where,
            order_by_columns=[])

        self.assertIsInstance(select_result, list, "result should be in list form")
        self.assertFalse(select_result, "result should be an empty list")




# tests for 'watch_status' table ?
# tests for other methods in self.mysql_service


if __name__ == '__main__':
    unittest.main()
