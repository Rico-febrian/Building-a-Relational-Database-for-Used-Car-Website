-- Populating The Database


-- Import dummy data for cities table
COPY
	cities
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\cities.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for products table
COPY
	products
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\products.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for users table
COPY
	users
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\users.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for advertisements table
COPY
	advertisements
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\advertisements.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for user searches table
COPY
	user_searches
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\user_searches.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for offers table
COPY
	offers
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\offers.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for reviews table
COPY
	reviews
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\reviews.csv'
DELIMITER ','
CSV
HEADER;


-- Import dummy data for reports table
COPY
	reports
FROM 
	'D:\PostgreSQL\Project\Used Car Website Database\reports.csv'
DELIMITER ','
CSV
HEADER;