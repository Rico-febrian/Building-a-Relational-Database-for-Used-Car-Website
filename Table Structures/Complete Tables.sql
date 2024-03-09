-- Cities Table
CREATE TABLE cities(
	city_id SERIAL PRIMARY KEY,
	city_name varchar(255) NOT NULL,
	address varchar(255) NOT NULL,
	location point NOT NULL
);

-- Products Table
CREATE TABLE products(
	product_id SERIAL PRIMARY KEY,
	brand varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	body_type varchar(100) NOT NULL,
	transmission varchar(100) NOT NULL,
	fuel_type varchar(20) NOT NULL,
	machine_capacity varchar(20) NOT NULL,
	production_year integer NOT NULL CHECK(production_year BETWEEN 2000 AND 2024),
	price numeric NOT NULL CHECK(price > 0)
);

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

-- Advertisements Table
CREATE TABLE advertisements(
	advertisement_id SERIAL PRIMARY KEY,
	product_id integer NOT NULL,
	user_id integer NOT NULL,
	title varchar(255) NOT NULL,
	description text NOT NULL,
	created_date date NOT NULL,
	advertisement_status varchar(10) NOT NULL CHECK(advertisement_status IN ('Sold', 'Available')),
	advertisement_view integer CHECK(advertisement_view >= 0),
	image varchar(255) NOT NULL,
	CONSTRAINT fk_advertisements_products
		FOREIGN KEY (product_id)
		REFERENCES products(product_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,
	CONSTRAINT fk_advertisements_users
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE									
);

-- User Searches Table
CREATE TABLE user_searches(
	search_id SERIAL PRIMARY KEY,
	user_id integer NOT NULL,
	keyword varchar(255) NOT NULL,
	search_date date NOT NULL,
	CONSTRAINT fk_searches_users
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

-- Offers Table
CREATE TABLE offers(
	offer_id SERIAL PRIMARY KEY,
	user_id integer NOT NULL,
	advertisement_id integer NOT NULL,
	offer_price numeric NOT NULL CHECK (offer_price > 0),
	offer_status varchar(10) NOT NULL CHECK (offer_status IN 
											 ('Accepted', 'Waiting', 'Rejected')),
	offer_date date NOT NULL,
	CONSTRAINT fk_offers_users
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,
	CONSTRAINT fk_offers_advertisements
		FOREIGN KEY (advertisement_id)
		REFERENCES advertisements(advertisement_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);


-- Reviews Table
CREATE TABLE reviews(
	review_id SERIAL PRIMARY KEY,
	user_id integer NOT NULL,
	advertisement_id integer NOT NULL,
	rating integer NOT NULL CHECK (rating BETWEEN 1 AND 5),
	review_description text,
	review_date date NOT NULL,
	CONSTRAINT fk_reviews_users
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,
		CONSTRAINT fk_reviews_advertisements
		FOREIGN KEY (advertisement_id)
		REFERENCES advertisements(advertisement_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

-- Reports Table
CREATE TABLE reports(
	report_id SERIAL PRIMARY KEY,
	user_id integer NOT NULL,
	advertisement_id integer NOT NULL,
	report_type varchar(50) NOT NULL CHECK (report_type IN
										   ('Spam','Fraud','Inappropriate Content','Other')),
	report_description text,
	report_date date NOT NULL,
	action_taken varchar(50) NOT NULL CHECK (action_taken IN
											('Warning','Hide Ads','Remove Ads',
											 'Account Suspended', 'Investigation')),
	CONSTRAINT fk_reports_users
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,
	CONSTRAINT fk_reports_advertisements
		FOREIGN KEY (advertisement_id)
		REFERENCES advertisements(advertisement_id)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);
