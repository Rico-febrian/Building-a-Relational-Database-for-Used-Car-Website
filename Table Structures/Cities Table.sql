-- Cities Table
CREATE TABLE cities(
	city_id SERIAL PRIMARY KEY,
	city_name varchar(255) NOT NULL,
	address varchar(255) NOT NULL,
	location point NOT NULL
);
