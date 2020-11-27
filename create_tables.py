from db_connection import DBConnection

def main():
    building_db = DBConnection('building_label_db')
    building_db.establish_connection()

    # Tabelle anlegen
    cursor = building_db.create_cursor("create")

    create_building_table = '''CREATE TABLE buildings
          ( ID              char(36) PRIMARY KEY     NOT NULL,
            picture_path    varchar(256),
            zip             numeric,
            city            varchar(30),
            street          varchar(30),
            number          integer,
            google_id       char(56),
            timestamp       timestamp); '''
    
    cursor.execute(create_building_table)
    building_db.connection.commit()
    building_db.close_cursor("create")

if __name__ == '__main__':
    main()
