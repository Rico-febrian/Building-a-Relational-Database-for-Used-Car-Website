-- Creating Transactional Query


-- Finding cars produced from 2015 onwards.

SELECT
	product_id,
	brand,
	model,
	production_year,
	price
FROM
	products
WHERE
	production_year >= 2015


-- Adding a new data entry to the offers table.

SELECT * FROM offers

INSERT INTO offers(offer_id, user_id, advertisement_id, offer_price, offer_status, offer_date)
VALUES(101, 42, 132, 480000000, 'Accepted', '2020-10-30')


-- Finding all cars sold by one account/user, sorted from the newest.

SELECT 
	p.product_id,
	p.brand,
	p.model,
	p.production_year,
	p.price,
	a.created_date
FROM products p
JOIN advertisements a USING (product_id)
WHERE user_id = 29
ORDER BY 6 DESC


-- Finding the cheapest used cars based on a keyword.

SELECT
	product_id,
	brand,
	model,
	production_year,
	price
FROM 
	products
WHERE
	model ILIKE '%avanza%'
ORDER BY 5 ASC


-- Finding used cars based on the nearest distance.

-- First, Create a function to calculate the haversine distance. 

CREATE FUNCTION haversine_distance(point1 POINT, point2 POINT)
RETURNS float AS $$
DECLARE
	lon1 float := radians(point1[0]);
	lat1 float := radians(point1[1]);
	lon2 float := radians(point2[0]);
	lat2 float := radians(point2[1]);
	
	dlon float := lon2 - lon1;
	dlat float := lat2 - lat1;

	a float;
	c float;
	r float := 6371;
	jarak float;
	
BEGIN
	-- Haversine Formula
	a := sin(dlat/2)^2 + cos(lat1) * cos(lat2) * sin(dlon/2)^2;
	c := 2 * asin(sqrt(a));
	jarak := r * c;
	
	RETURN jarak;
END;
$$ LANGUAGE plpgsql;


-- Finding the nearest car with city id = 5

SELECT
	p.product_id,
	c.city_id,
	p.brand,
	p.model,
	p.production_year,
	p.price,
	haversine_distance((SELECT location from cities WHERE city_id = 5), c.location) AS distance
FROM 
	products p 
JOIN
	advertisements a USING (product_id)
JOIN 
	users u USING (user_id)
JOIN 
	cities c ON u.city_id = c.city_id
ORDER BY
	distance ASC
		
		