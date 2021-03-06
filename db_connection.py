import psycopg2
import json
from configparser import ConfigParser

class DBConnection:

    def __init__(self, database_name):
        self.__database_name = database_name
        self.__read_db_config()
        self.__cursors = {}

    def __del__(self):
                if(self.connection):
                    self.connection.close()
                    print("PostgreSQL connection is closed")

    # Read configuration from server.ini
    def __read_db_config(self):
        self.__db_config = ConfigParser()
        self.__db_config.read('server.ini')

    # Open Database connection
    def establish_connection(self):
        self.__connection = psycopg2.connect(   user = self.__db_config["USER"]["user"],
                                                password = self.__db_config["USER"]["password"],
                                                host = self.__db_config["SERVER"]["host"],
                                                port = self.__db_config["SERVER"]["port"],
                                                database = self.database_name )

    def __get_database_name(self):
        return self.__database_name

    database_name = property(__get_database_name)

    def __get_connection(self):
        return self.__connection

    connection = property(__get_connection)

    # Cursor handling
    def create_cursor(self, name):
        if name not in self.__cursors:
            self.__cursors[name] = DBCursor(self.connection)
            return self.__cursors[name].cursor

    def close_cursor(self, name):
        self.__cursors.pop(name)


# Handling of cursors
class DBCursor:

    def __init__(self, connection):
        self.__cursor = connection.cursor()

    def __del__(self):
        print("Cursor closed")
        self.__cursor.close()

    def __get_cursor(self):
        return self.__cursor

    cursor = property(__get_cursor)


def main():

    # Test functionality
    building_db_test = DBConnection('building_label_db')
    building_db_test.establish_connection()

    try:
        cursor = building_db_test.create_cursor("test")
        # Print PostgreSQL Connection properties
        print ( building_db_test.connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")

        building_db_test.close_cursor("test")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


if __name__ == '__main__':
    main()

