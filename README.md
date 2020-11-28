# Analysis-of-energy-inefficient-buildings

Rising Prices, shrinking resources, liability for climate and environment are just a few reasons to challenge our energy consumption and approach a more thoughtful and economical way. Buildings in Switzerland are responsible for about 45 % of energy usage. EMPA would like to change this by combining open data and modern technologies like neural network classification to evaluate buildings worth a structural energy efficiency upgrade and reduce energy loss in the city Lucerne. 

This challenge is all about improving the process of analysing building structures in the city of Lucerne. Whether it is to build a solid data infrastructure, a tool for optimized data classification or an innovative analysis model, the limit is your creativity. We already developed two interesting ideas, which you can tackle or use to get you an idea what kind of puzzle pieces we are looking in the process:   

###Idea 1: 
Create a building database - To train models around the energy consumption of a building it is crucial to rely on a broad database of good quality. You build the foundation by acquiring data from Google Street View data (API) or another platform. In this process it would be interesting to see a working workflow from acquiring pictures and extracting relevant information to pool all information in an easily accessible database. Relevant information could be: “Picture of the building”, “coordinates”, “address”, “building end-use” and/or other information.

###Idea 2: 
Picture Labelling App - Neural network classification needs labelled data to train and achieve a reliable machine learning model. You could create an application prototype that will make it possible to document information and label buildings features and structures like doors, walls, etc and connect them to the physical address of the building. The following information is of special interest in this context:

- Window to wall ratio: By defining the window and door areas. It is possible to calculate the window to wall ratio.
- Building end-use: In the picture there can be seen if e.g. a restaurant is located in the building.
- Facade albedo: the colour of the building can help to determine the albedo of the build

# Documentation 
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

## Authors 
Dominik Vasquez, Stephan Wernli, Luca Casuscelli, Jonas Zürcher 

