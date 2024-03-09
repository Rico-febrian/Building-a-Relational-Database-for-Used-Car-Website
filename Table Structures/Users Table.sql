-- Users Table
CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	username varchar(100) UNIQUE NOT NULL,
	first_name varchar(255) NOT NULL,
	last_name varchar(255),
	email varchar(255) UNIQUE NOT NULL,
	password varchar(255) NOT NULL CHECK(LENGTH(password) >= 8),
	contact varchar(50) NOT NULL,
	registration_date date NOT NULL,
	city_id integer NOT NULL,
	user_status varchar(10) NOT NULL CHECK(user_status IN('Active', 'Inactive')) DEFAULT 'Active',
	CONSTRAINT fk_users_cities
		FOREIGN KEY (city_id)
		REFERENCES cities(city_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);
