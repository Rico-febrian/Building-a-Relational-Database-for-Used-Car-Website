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
