# Analysis-of-energy-inefficient-buildings
## Project description 
Rising Prices, shrinking resources, liability for climate and environment are just a few reasons to challenge our energy consumption and approach a more thoughtful and economical way. Buildings in Switzerland are responsible for about 45 % of energy usage. EMPA would like to change this by combining open data and modern technologies like neural network classification to evaluate buildings worth a structural energy efficiency upgrade and reduce energy loss in the city Lucerne. For the performance of image analysis and model training we first need a solid infrastructure to retrieve and store data. With our project we would like to tackle this challenge. 

## Technical Base
The application is using Python and PostgreSQL to save the data provided by the google API. The connection data like username, password, database name, etc. are stored in server.ini. 
## Architecture
There are several classes that manage the database connection, the creation of table entries and the saving of the pictures to the file system.
The semantic key to access a picture is given through its address. The zip-code, the street and the building number are used to access the data sets and check whether an entry exists or not. If a building does not exist yet in the database a uuid-key is generated and used as a primary key for the building. The picture is saved with the “uuid”.jpg as filename. 
## Classes
•	DBConnection: Manages the DB connections and handles DB cursors

•	DBCursor: little Proxy for Cursors

•	Building: The Buillding class is meant to manage the access and the storing of pictures and meta data.

•	ImageExtractor: Interface to Google Street View API

## Files
•	addresses.txt: some sample addresses for testing and mockup

•	Building_database.py: home of Class Building

•	create_tables.py: Creates the needed DB tables

•	db_connection.py: home of Classes DBConnection and DBCursor

•	google_street_extractor.py: home of Class ImageExtractor

•	key.txt: not used in prototype. Is supposed to contain the Google Street View API key

•	main.py: Mockup of functionality. Reads addresses from addresses.txt and extracts data and images from google street view and saves them in the database using Classes ImageExtractor and Building

•	Readme.md…

•	requirements.txt: contains all necessary requirements (Anaconda style)

•	server.ini: contains all configuration data (to be adjusted by customer by write_db_config.py)

•	test_retrieve.py: Test of extraction of data and images that were written with main.py

•	write_db_config.py: writes parameters to server.ini

## Data
The data was retrieved with a Google API Key 

## Authors 
Dominik Vasquez, Stephan Wernli, Luca Casuscelli, Jonas Zürcher 

