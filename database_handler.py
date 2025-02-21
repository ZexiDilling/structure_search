import configparser
import sqlite3


class DataBaseFunctions:
    def __init__(self, config):
        self.conn = None
        self.cursor = None
        self.database = config["Database"]["database"]

    def __str__(self):
        """Control all database function, as sqlite3 is terrible for writing to and from"""

    @staticmethod
    def _list_columns(data):
        """
        Genera a list of headlines/keys from a dict.

        :param data: A dict over the data
        :type data: dict
        :return: a list of headlines/keys from dict
        :rtype: list
        """
        return [clm for clm in data]

    @staticmethod
    def _add_place_holders(columns):
        """
        make a string of "?" depending on how many columns/headlines/keys a dict have.

        :param columns: list of columns/headlines/keys
        :type columns: list
        :return: A string of "?" for SQlite3 to use for adding values
        :rtype: str
        """
        return ",".join("?" for _ in columns)

    @staticmethod
    def _add_layout(table_name, place_holders):
        """
        Makes a string that SQlite3 can use to add data

        :param table_name: name of table
        :type table_name: str
        :param place_holders: String of "?" one "?" per headline the table has
        :type place_holders: str
        :return: A string for SQlite to use.
        :type: str
        """
        return f"INSERT INTO {table_name} VALUES({place_holders})"

    @staticmethod
    def _data_layout(data, column_names):
        """
        Formatting a list for SQlite3 to add to the database

        :param data: The data that needs to be added
        :type data: dict
        :param column_names: List of column names
        :type column_names: list
        :return: List of data and values.
        :rtype: list
        """
        return [data[name] for name in column_names]

    def _add_data_to_table(self, layout, data):
        """
        Function that adds data to the database

        :param layout: String with table name, and "?" for each value that needs to be added
        :type layout: str
        :param data: List of values that needs to be added
        :type data: list
        :return: Data added to a table
        """

        try:
            self.cursor.execute(layout, data)
        except sqlite3.IntegrityError as error:
            print(f"{error} - {layout} - {data}")
            #print("ERROR") # NEEDS TO WRITE REPORT OVER ERRORS TO SEE WHY DATA WAS NOT ADDED!!!
            # EITHER DUE TO DUPLICATES OR MISSING REFERENCE(FOREIGN KEY)
        self.conn.commit()
        self.cursor.close()


    def add_records_controller(self, table_name, data, counter=None):
        """
        Adds data to the database, main access point to multiple functions

        :param table_name: Name of the table where the data needs to be added
        :type table_name: str
        :param data: The data, in dicts form, that needs to be added to the database
        :type data: dict
        :return: Data added to the database
        """
        self.create_connection()
        list_columns = self._list_columns(data)
        if "Row_Counter" in list_columns:
            rows = self.number_of_rows(table_name)
            # This is due to me deleting some data that should not have been deleted, but should have been changed
            # active to zero .
            if table_name == "compound_mp":
                rows += 384
            data["Row_Counter"] = rows + 2
        place_holder = self._add_place_holders(list_columns)
        layout = self._add_layout(table_name, place_holder)
        data_layout = self._data_layout(data, list_columns)
        self._add_data_to_table(layout, data_layout)

    def update_vol(self, source_table, vol, barcode_source, row_id):
        """
        Updates volumes in the database

        :param source_table: Where the compound came from
        :type source_table: str
        :param vol: How much compound was taken
        :type vol: int
        :param barcode_source: Where is the compound going
        :type barcode_source: str
        :param row_id: The id of the row in the database
        :type row_id: str
        :return: An updated database
        """
        table_row = f"UPDATE {source_table} SET volume = volume - {vol} WHERE {row_id} = {barcode_source} "
        self.submit_update(table_row)

    def update_database_items(self, source_table, table_data, index_key_data, index_key_headline):
        """
        Updates a row in the database
        :param source_table: The table
        :type source_table: str
        :param table_data: A dict of clm headlines and their values
        :type table_data: dict
        :param index_key_data: The index value, as to what row to update
        :type index_key_data: str or int
        :param index_key_headline: The headline for the index value
        :type index_key_headline: str
        :return:
        """
        # table_row_string = f"UPDATE {source_table} SET"
        # for headlines in table_data:
        #     table_row_string += f" {headlines} = '{ {table_data[headlines]} }', "
        # table_row_string = table_row_string.removesuffix(", ")
        # table_row_string += f" WHERE {headline} = '{table_index_value}'"
        table_row_string = f"UPDATE {source_table} SET "
        for column, value in table_data.items():
            # Ensure string values are enclosed in single quotes and properly escaped
            formatted_value = value.replace("'", "''") if isinstance(value, str) else value
            table_row_string += f"{column} = '{formatted_value}', "
        table_row_string = table_row_string.removesuffix(", ")
        table_row_string += f" WHERE {index_key_headline} = {index_key_data}"
        self.submit_update(table_row_string)

    def rename_record_value(self, table, headline_for_changing_value, headline_for_indicator_value, indicator_value,
                            new_value):
        """
        Renames a record based on the name of value of the record
        :param table: The table where the data is located
        :type table: str
        :param headline_for_changing_value: the column headline for the data that needs to be changed
        :type headline_for_changing_value: str
        :param headline_for_indicator_value: The headline for the indicator value
        :type headline_for_indicator_value: str
        :param indicator_value: A value to find the right row from
        :type indicator_value: str
        :param new_value: The new value, that needs to be changed to
        :type new_value: str
        :return: An updated database
        """
        table_update = f'UPDATE {table} SET {headline_for_changing_value} = "{new_value}" WHERE {headline_for_indicator_value} = "{indicator_value}"'

        self.submit_update(table_update)

    def find_data_double_lookup(self, table, data_1_value, data_2_value, data_1_headline, data_2_headline):
        """
        Finds data in the database depending on two lookup values

        :param table: What table the data should be in
        :type table: str
        :param data_1_value: Barcode of the plate
        :type data_1_value: str
        :param data_2_value: Compound ID
        :type data_2_value: int
        :param data_1_headline: Headline of the plate-column in the table
        :type data_1_headline: str
        :param data_2_headline: Headline for the compound id in the table
        :type data_2_headline: str
        :return: Data from the database
        :rtype: dict
        """
        find = f"SELECT rowid, * FROM '{table}' WHERE {data_1_headline} = '{data_1_value}' AND {data_2_headline} = '{data_2_value}'"
        return self.fetch(find)

    def find_data_single_lookup(self, table, data_value, headline):
        """
        Finds data in the database depending on a single lookup value

        :param table: What table are the plates in
        :type table: str
        :param data_value: The value of the thing you are looking for
        :type data_value: str
        :param headline: Headline for the coloumn where  the data is, in the table
        :type headline: str
        :return: Data from the database
        :rtype: dict
        """

        if type(data_value) == str:
            find = f"SELECT rowid, * FROM '{table}' WHERE {headline} = '{data_value}' "
        else:
            find = f"SELECT rowid, * FROM '{table}' WHERE {headline} = '{data_value}' "
        return self.fetch(find)

    def delete_records(self, table, headline, data_value):
        """
        Deletes a record from the database
        :param table: What table are the plates in
        :type table: str
        :param data_value: The value of the thing you are looking for
        :type data_value: str
        :param headline: Headline for the coloumn where  the data is, in the table
        :type headline: str
        :return:
        """

        delete = f"DELETE FROM {table} WHERE {headline} = '{data_value}'"
        self.create_connection()
        self.cursor.execute(delete)
        self.conn.commit()
        self.cursor.close()

    def run(self):
        pass

    #table generator... maybe not needed
    # @staticmethod
    # def generate_columns(columns):
    #     return ", ".join(headline for headline in columns)
    #
    # @staticmethod
    # def setup_columns(column_names):
    #     temp_list = []
    #     for index, headline in column_names:
    #         if index != 0:
    #             if headline == "Volume":
    #                 temp_list.append(f"{headline} REAL")
    #             else:
    #                 temp_list.append(f"{headline} TEXT")
    #     return temp_list
    #
    # @staticmethod
    # def setup_name(table_name):
    #     if table_name.isnumeric():
    #         return f"compound_{table_name}"
    #     else:
    #         return table_name
    #
    # @staticmethod
    # def generate_table_layout(table_name, columns_names):
    #     return f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_names});"
    #
    # def table_generator(self, dict_data):
    #     try:
    #         table_name = dict_data["DestinationBarcode"]
    #     except KeyError:                                            # Incase a table per compound is needed
    #         table_name = f"compound_{dict_data['barcode']}"
    #     column_list = self.setup_columns(dict_data)
    #     columns = self.generate_columns(column_list)
    #     table = self.generate_table_layout(table_name, columns)
    #     self.submit_update(table)

    def fetch(self, data):
        """
        Create a connection to the database, execute the search and gets data out of  the database

        :param data: The data the user is looking for
        :type data: str
        :return: all records that fits the data
        :rtype: dict
        """
        self.create_connection()
        self.cursor.execute(data)
        records = self.cursor.fetchall()
        self.cursor.close()
        return records

    def submit_update(self, table_row, new_value=None, old_value=None):
        """
        Connect to the database, Updates the database and closes the connection

        :param table_row: Data that needs  to be updated
        :type table_row: str
        :return: commits updates to the database
        """

        self.create_connection()
        try:
            self.cursor.execute(table_row)
        except sqlite3.IntegrityError as e:
            print(f"sql error - {e}")
        self.conn.commit()
        self.cursor.close()

    def create_connection(self):
        """
        Create a connection to the database

        :return: A connection to the database
        :
        """
        self.conn = sqlite3.connect(self.database)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
        # NEEDS TO BE ACTIVE AT STARTUP
        # return self.conn

    def list_of_all_tables(self):
        """
        Gets a list of all the tables in the database

        :return: A list of all the tables in the database
        :rtype: list
        """
        return [tables for tables in self.cursor.execute("SELECT name FROM sqlite_master  WHERE type='table';")]

    def number_of_rows(self, table):
        """
        Counts rows in database.
        Missing to check for active samples

        :param table: Table name
        :type table: str
        :return: number of rows in table.
        :rtype: int
        """
        number = f"SELECT COUNT(*) from {table}"
        self.create_connection()
        self.cursor.execute(number)
        return self.cursor.fetchone()[0]

    def join_table_controller_old(self, search_limiter, table_1="compound_main", table_2="compound_mp",
                              shared_data="compound_id"):
        """
        Joins two tables together to create a new temp table

        :param min_volume: Minimum volume needed for a compound
        :type min_volume: int
        :param table_1: Table 1 of 2 for joining together
        :type table_1: str
        :param table_2: Table 2 of 2 for joining together
        :type table_2: str
        :param shared_data: The data they share
        :type shared_data: str
        :return: Rows of data where the two tables matches.
        :rtype: dict
        """
        min_volume = search_limiter["volume"]["value"]
        sql_join = f"SELECT {table_1}.compound_id, mp_barcode, mp_well, smiles, {table_2}.volume  FROM {table_1} " \
                   f"JOIN " f"{table_2} ON {table_1}.{shared_data} = {table_2}.{shared_data} WHERE {min_volume}<" \
                   f"{table_2}.volume;"

        return self._row_creator(sql_join)

    def join_table_controller(self, search_limiter):
        """
        Joins two tables together to create a new temp table

        :param min_volume: Minimum volume needed for a compound
        :type min_volume: int
        :param table_1: Table 1 of 2 for joining together
        :type table_1: str
        :param table_2: Table 2 of 2 for joining together
        :type table_2: str
        :param shared_data: The data they share
        :type shared_data: str
        :return: Rows of data where the two tables matches.
        :rtype: dict
        """
        selector_1 = ""
        selector_2 = ""
        binder = ""
        for index, values in enumerate(search_limiter):
            if index == 0:
                table_1 = values
                selector_1 = self._where_clause_writer(search_limiter[values], values)
            if index == 1:
                table_2 = values
                selector_2 = self._where_clause_writer(search_limiter[values], values)
            shared_data = search_limiter["shared_data"]

        if selector_1 and selector_2:
            binder = "AND"


        sql_join = f"SELECT * FROM {table_1} JOIN {table_2} ON {table_1}.{shared_data} = {table_2}.{shared_data} " \
                   f"{selector_1} {binder} {selector_2}"

        print(f"sql_join - {sql_join}")
        return self._row_creator(sql_join)

    @staticmethod
    def _where_clause_writer(search_limiter, join_table=None):

        if join_table:
            table = f"{join_table}."
        else:
            table = ""

        if search_limiter:
            final_text = "WHERE"
            for conditions in search_limiter:
                if search_limiter[conditions]["use"]:
                    if search_limiter[conditions]["value"]:
                        if search_limiter[conditions]['operator'] == "IN":
                            target_string = "("
                            for values in search_limiter[conditions]['value']:
                                target_string += f"'{values}'"
                                target_string += ","
                            target_string = target_string.removesuffix(",")
                            target_string += ")"

                            final_text += f" {table}{search_limiter[conditions]['target_column']} {search_limiter[conditions]['operator']} " \
                                          f"{target_string}"
                        else:
                            final_text += f" '{search_limiter[conditions]['value']}' {search_limiter[conditions]['operator']} " \
                                          f"{search_limiter[conditions]['target_column']}"
                        final_text += f" AND"

            final_text = final_text.removesuffix(" AND")
            final_text = final_text.removesuffix("WHERE")

        else:
            final_text = ""

        return final_text

    def return_table_data_from_list(self, table, search_list, search_list_clm, specific_clm):
        # Convert the list of selected assay names into a comma-separated string for the SQL query
        selected_assays_str = ", ".join([f"'{assay_name}'" for assay_name in search_list])

        from_string = ""
        if specific_clm is not None:
            for clm_names in specific_clm:
                from_string += f"{clm_names}, "
            from_string = from_string.removesuffix(", ")
        else:
            from_string = "*"
        # SQL query to select data from the "assay_runs" table where the "assay_name" is in the selected_assays list
        temp_table = f"SELECT {from_string} FROM {table} WHERE {search_list_clm} IN ({selected_assays_str})"

        return self._row_creator(temp_table)

    def grab_table_headers(self, table):

        temp_data = f"SELECT * FROM {table}"
        self.create_connection()
        cursor = self.cursor.execute(temp_data)
        self.cursor.close()
        return [description[0] for description in cursor.description]

    def return_table_data(self, table, search_limiter):
        """
        Gets all information from a table, there is over "min_volume" left

        :param table: Table the data needs  to be pulled from
        :type table: str
        :param search_limiter: Threshold for fecthing data
        :type search_limiter: int
        :return: Rows of data, based on min_volume
        :rtype: dict
        """
        if search_limiter:
            selector = self._where_clause_writer(search_limiter)
        else:
            selector = None
        if selector:
            temp_table = f"SELECT * FROM {table} {selector}"
        else:
            temp_table = f"SELECT * FROM {table}"
        return self._row_creator(temp_table)

    def find_column_data(self, table, clm_header):
        """
        Gets all data from a single column from a table

        :param table: Table the data needs  to be pulled from
        :type table: str
        :param clm_header: The headline for the column
        :type clm_header: str
        :return: the row for the data
        :rtype: dict
        """
        temp_table = f"SELECT {clm_header} FROM {table} "
        return self._row_creator(temp_table)

    def _row_creator(self, data):
        """
        Gets data from the database based on criteria

        :param data: Data that needs to be found.
        :type data: str
        :return: Rows of data from the database
        :rtype: dict
        """
        rows = {}
        self.create_connection()
        try:
            self.cursor.execute(data)
        except:
            return [[]]
        else:

            records = self.cursor.fetchall()
            headers = self.cursor.description
            for data in records:

                rows[data[0]] = {}
                for index, header in enumerate(headers):
                    rows[data[0]][header[0]] = data[index]

            self.cursor.close()
            return rows


if __name__ == "__main__":
    pass


