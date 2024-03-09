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
