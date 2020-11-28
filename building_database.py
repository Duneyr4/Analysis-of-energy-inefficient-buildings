import uuid
from db_connection import DBConnection
import datetime 
import cv2
from configparser import ConfigParser
import os
import matplotlib.pyplot as plt

class Building:

    def __init__(self, zip, city, street, number):
        self.__zip = zip
        self.__street = street
        self.__number = number
        self.__city = city
        self.__uuid = None
        self.__picture_path = None
        self.__timestamp = None
        self.__google_id = None

        # Get configuration from server.ini
        self.__read_config()
        self.__path = self.__config["PICTURES"]["path"]
        self.__db = self.__config["DATABASE"]["database"]

        # Establish database connection
        self.__building_db = DBConnection(self.__db)
        self.__building_db.establish_connection()

        # Get Data from DB
        if self.__read_db():
            self.__exists_db = True
        else:
            self.__exists_db = False
            self.__uuid = uuid.uuid1()


    def __get_uuid(self):
        return self.__uuid

    uuid = property(__get_uuid())


    def __read_config(self):
        self.__config = ConfigParser()
        self.__config.read('server.ini')


    def __read_db(self):
        
        # Cursor erzeugen
        cursor_uuid = uuid.uuid1()
        cursor = self.__building_db.create_cursor(cursor_uuid)

        select_building = '''   select
                                    id,
                                    picture_path,
                                    zip,
                                    city,
                                    street,
                                    number,
                                    timestamp,
                                    google_id
                                from buildings 
                                where zip = %s
                                and   street = %s
                                and   number = %s; '''
        
        cursor.execute(select_building, (self.__zip, self.__street, self.__number))
        building = cursor.fetchall()
        self.__building_db.connection.commit()
        self.__building_db.close_cursor(cursor_uuid)

        if len(building) > 1:
            raise Exception("Multiple Buildings found! ZIP: " + str(self.__zip) + "; Street: " + self.__street + "; Number: " + str(self.__number) )
        elif len(building) == 0:
            return False
        elif len(building) == 1:
            self.__uuid = building[0][0]
            self.__picture_path = building[0][1]
            self.__timestamp = building[0][6]
            self.__google_id = building[0][7]
            return True

    def save_picture(self, picture, google_id = None):
        picture_name = str(self.__uuid) + ".jpg"
        self.__picture_path = os.path.join(self.__path, picture_name)
        self.__google_id = google_id

        self.__write_picture(picture, self.__picture_path)

        timestamp = datetime.datetime.now()

        cursor_uuid = uuid.uuid1()
        cursor = self.__building_db.create_cursor(cursor_uuid)

        if self.__exists_db:
            update_building = '''   Update buildings set 
                                        picture_path = %s,
                                        timestamp = %s,
                                        google_id = %s 
                                    where id = %s '''
            cursor.execute(update_building, (self.__picture_path, timestamp, self.__google_id, str(self.__uuid)))

        else:
            insert_building = '''   insert into buildings ( id, picture_path, zip, city, street, number, timestamp, google_id )
                                    values (%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(insert_building, (str(self.__uuid), self.__picture_path, self.__zip, self.__city, self.__street, self.__number, timestamp, self.__google_id))

        self.__building_db.connection.commit()
        self.__building_db.close_cursor(cursor_uuid)


    def get_picture(self):
        if self.__picture_path:
            return cv2.imread(self.__picture_path)


    def __write_picture(self, picture, path):
        result = cv2.imwrite(path, picture)
        if result != True:
            raise Exception("Picture could not be saved to directory!")

    
    def get_building(self):
        return  self.__uuid, self.__picture_path, self.__zip, self.__city, self.__street, self.__number, self.__timestamp, self.__google_id, self.get_picture()


def save_building(zip, city, street, number, picture, google_id = None):
    building_save = Building(zip, city, street, number)
    building_save.save_picture(picture, google_id)
    return building_save.uuid


def open_building(zip,city,street,number):
    building_open = Building(zip, city, street, number)
    return building_open.get_building()


def main():
    
    # Test save 1...
    picture = cv2.imread("C:/Users/domin/OneDrive/Projekte/Python Projekte/Style Transfer/generated_images/Dominik_Kubismus_final.png")
    save_building('8400', 'Winterthur', 'Teststrasse', 1, picture, "TEST1")

    # Test save 2...
    picture = cv2.imread("C:/Users/domin/OneDrive/Projekte/Python Projekte/Style Transfer/generated_images/Luca_Haringfinal.png")
    save_building('8000', 'Zürich', 'Teststrasse', 1, picture, "TEST2")

    # Test save 3...
    picture = cv2.imread("C:/Users/domin/OneDrive/Projekte/Python Projekte/Style Transfer/generated_images/serowfinal.png")
    save_building('8001', 'Zürich', 'Teststrasse', 1, picture, "TEST3")

    # Test save 4...
    picture = cv2.imread("C:/Users/domin/OneDrive/Projekte/Python Projekte/Style Transfer/generated_images/landschaft1_haring_final.png")
    save_building('8004', 'Zürich', 'Feststrasse', 1, picture, "TEST4")


    # # Test read 3
    id3, pp3, zip3, city3, street3, num3, ts3, gid3, pic3 = open_building('8000', 'Zürich', 'Teststrasse', 1)

if __name__ == '__main__':
    main()






        


