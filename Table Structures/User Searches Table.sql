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
