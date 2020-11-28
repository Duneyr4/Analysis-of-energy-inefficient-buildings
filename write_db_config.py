from configparser import ConfigParser

def write_db_config():
    db_config = ConfigParser()

    db_config["USER"] = {
        "user": "empa_nsuper",
        "password": "a9C&wVgmg(&:y_124OT?Os",
    }

    db_config["SERVER"] = {
        "host": "127.0.0.1",
        "port": "5432"
    }

    db_config["DATABASE"] = {
        "database": "building_label_db"
    }

    db_config["PICTURES"] = {
        "path": "C:/Users/domin/OneDrive/Studium/Projekte/Analysis-of-energy-inefficient-buildings/pictures/"
    }

    with open('server.ini', 'w') as config:
        db_config.write(config)

write_db_config()