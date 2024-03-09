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
