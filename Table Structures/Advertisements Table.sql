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
