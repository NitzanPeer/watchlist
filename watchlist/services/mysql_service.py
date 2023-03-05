import mysql.connector

class MySQLService:

    _instances = {}

    connection = None
    cursor = None

    # this method is a helper in using the class as a singleton
    # https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    def __new__(cls, *args, **kwargs):

        instance_key = str(kwargs)

        if instance_key not in cls._instances:
            cls._instances[instance_key] = super(MySQLService, cls).__new__(cls)
        return cls._instances[instance_key]

    def __init__(self, host="localhost", user="root", password="123", port=1110, database="movie_db"):

        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.database=database

        if not self.connection:
            self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            port = self.port,
            database = self.database
        )

        self.cursor = self.connection.cursor(dictionary=True)

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def select_one(self, table_name, columns=[], where_data=None, order_by_columns=[]):
        self.__raw_select(table_name, columns, where_data, order_by_columns, {'count': 1})
        return self.cursor.fetchone()

    def select_all(self, table_name, columns=[], where_data=None, order_by_columns=[], limit={}):
        self.__raw_select(table_name, columns, where_data, order_by_columns, limit)
        return self.cursor.fetchall()

    def insert(self, table_name, insert_data):

        key_list = self.__dict_to_key_list(insert_data)
        value_list = self.__dict_to_value_list(insert_data)

        try:
            self.raw_query(f"INSERT INTO {table_name} ({key_list}) VALUES ({value_list});")
            result = self.cursor.lastrowid

        except mysql.connector.IntegrityError:
            result = False

        return result

    def update(self, table_name, set_data, where_data=None):

        set_clause = self.__set_clause_handling(set_data)

        if not set_clause:
            return False

        update_set_clause = f"UPDATE {table_name} SET {set_clause}"

        if not where_data:
            self.raw_query(f"{update_set_clause};")

        else:
            where_clause = self.__where_clause_handling(where_data)
            self.raw_query(f"{update_set_clause} {where_clause};")

        return self.cursor.rowcount

    def delete(self, table_name, where_data):

        delete_from_clause = f"DELETE FROM {table_name}"

        where_clause = self.__where_clause_handling(where_data)

        self.raw_query(f"{delete_from_clause} {where_clause};")

        return self.cursor.rowcount

    def is_table_exist(self, table_name):

        self.raw_query(f"SHOW TABLES LIKE {table_name};", False)
        result = self.cursor.fetchone()
        return bool(result)

    def raw_query(self, query, is_commit=True):
        #TODO: test prints:
        print(query)
        print("=========")
        self.cursor.execute(query)
        if is_commit:
            self.connection.commit()

    def __raw_select(self, table_name, columns=[], where_data=None, order_by_columns=[], limit={}):

        columns_as_string = ", ".join(columns) if columns else '*'

        query = f"SELECT {columns_as_string} FROM {table_name}"


        if where_data:
            query += " "
            query += self.__where_clause_handling(where_data)


        if order_by_columns:

            counter = 0
            order_by_clause = "ORDER BY"

            for order_by in order_by_columns:

                order = order_by.get('order', 'ASC')
                # order = order_by['order'] if 'order' in order_by and order_by['order'] else 'ASC'
                order_by_clause += f" {order_by['column']} {order}"
                counter += 1
                if counter != len(order_by_columns):
                    order_by_clause += ","

            query += f" {order_by_clause}"

        if limit:
            offset_string = f"{limit['offset']}, " if limit.get('offset') else ''
            limit_clause = f"LIMIT {offset_string}{limit['count']}"

            query += f" {limit_clause}"

        query += ";"

        self.raw_query(query, False)

    def __dict_to_key_list(self, dictionary):
        return ', '.join(list(dictionary.keys()))

    # TODO: fix null treated as a string (prob lies in the return making the entire thing a str, need to change the method from slicing to something else)
    def __dict_to_value_list(self, dictionary):

        # test prints:
        # print("dict:")
        # print(dictionary)
        # print("genres:")
        # print(dictionary['genres'])
        # print(type(dictionary['genres']))

        new_list = []

        for key in dictionary:

            converted_value = self.__convert_python_value_to_sql(dictionary[key])
            new_list.append(converted_value)
        # test print:
        # print(f"before - {new_list}")
        # print(f"after - {str(', '.join(new_list))}")
        # print(f"type - {type(str(', '.join(new_list)))}")
        # print(f"slicing - {str(new_list)[1:-1]}")

        return str(', '.join(new_list))
        # if len(new_list) > 1 else
        # return str(new_list)[1:-1]


    def __convert_python_value_to_sql(self, item_to_convert):

        if isinstance(item_to_convert, bool):
            item_to_convert = int(item_to_convert)

        if isinstance(item_to_convert, str) and len(item_to_convert) > 0:
            item_to_convert = item_to_convert.replace("'", "\\'")
            item_to_convert = f"'{item_to_convert}'"

        if item_to_convert == None or item_to_convert == '':
            item_to_convert = 'null'


        return item_to_convert


    def __set_clause_handling(self, set_data):

        set_clause = ""

        for key in set_data:
            if isinstance(set_data[key], str):
                set_clause += f"{key} = '{set_data[key]}'"
            else:
                value = self.__convert_python_value_to_sql(set_data[key])
                set_clause += f"{key} = {value}"

            set_clause += ", "

        return set_clause[:-2] if set_clause else set_clause

    def __where_clause_handling(self, where_data):

        where_clause = ""

        for dictionary in where_data:

            column = f"{dictionary['column']} "
            operator = f"{dictionary['operator']} "

            if isinstance(dictionary['value'], str):
                value = f"'{dictionary['value']}'"
            else:
                value = self.__convert_python_value_to_sql(dictionary['value'])
                value = f"{value}"

            where_clause += column + operator + value
            where_clause += " AND "

        return f"WHERE {where_clause[:-5]}"
