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
