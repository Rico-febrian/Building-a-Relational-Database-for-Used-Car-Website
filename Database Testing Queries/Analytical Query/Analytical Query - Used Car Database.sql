-- Analytical Query


-- Ranking the popularity of car models based on the number of offers/bids.

WITH count_offer AS(
	SELECT 
		p.model,
		COUNT(o.offer_id) AS count_offer
	FROM 
		offers o
	JOIN
		advertisements a USING (advertisement_id)
	JOIN
		products p USING (product_id)
	GROUP BY 1
),
count_product AS(
	SELECT 
		p.model,
		COUNT(p.product_id) AS count_product
	FROM 
		products p 
	GROUP BY 1
)
SELECT 
	co.model,
	cp.count_product,
	co.count_offer
FROM 
	count_offer co
JOIN
	count_product cp ON co.model = cp.model
ORDER BY 3 DESC


-- Comparing car prices based on the average price per city.

SELECT
	c.city_name,
	p.brand,
	p.model,
	p.production_year,
	p.price,
	AVG(p.price) OVER(PARTITION BY c.city_name) AS avg_car_city
FROM
	products p
JOIN
	advertisements a USING (product_id)
JOIN 
	users u USING (user_id)
JOIN 
	cities c USING (city_id)
ORDER BY 6 ASC


-- For a specific car model, finding the comparison of the date 
-- when a user placed a bid with the next bid date and the offered price.

WITH offer_details AS(
	SELECT
		p.product_id,
		p.model,
		o.user_id,
		o.offer_date AS first_offer_date,
		LEAD(o.offer_date) OVER(PARTITION BY o.user_id, p.model ORDER BY o.offer_date) AS next_offer_date,
		o.offer_price AS first_offer_price,	
		LEAD(o.offer_price) OVER(PARTITION BY o.user_id, p.model ORDER BY o.offer_date) AS next_offer_price
	FROM
		offers o
	JOIN 
		advertisements a USING (advertisement_id)
	JOIN
		products p USING (product_id)
)
SELECT
	product_id,
	model,
	user_id,
	first_offer_date,
	next_offer_date,
	first_offer_price,
	next_offer_price
FROM 
	offer_details
ORDER BY 1,2


-- Comparing the percentage difference in average car prices based on their models 
-- and the average bid prices offered by customers in the last 6 months.

WITH avg_price AS(
	SELECT
		model,
		AVG(price) AS avg_price
	FROM 
		products
	GROUP BY 1
),
avg_offer AS(
	SELECT
		p.model,
		EXTRACT(YEAR FROM o.offer_date) AS year,
		EXTRACT(MONTH FROM o.offer_date) AS month,
		AVG(o.offer_price) AS avg_offer_6month
	FROM 
		offers o
	JOIN
		advertisements a USING (advertisement_id)
	JOIN 
		products p USING (product_id)
	WHERE
		o.offer_date >= DATE '2023-07-01' AND o.offer_date < DATE '2024-01-01'
	GROUP BY 1,2,3
)
SELECT
	ao.month,
	ap.model,
	ROUND(ap.avg_price, 3) AS avg_price,
	ROUND(ao.avg_offer_6month, 3) AS avg_offer_6month,
	ROUND(ap.avg_price - ao.avg_offer_6month, 3) AS difference,
	ROUND(((ap.avg_price - ao.avg_offer_6month)/ap.avg_price), 3) * 100 AS difference_percent
FROM 
	avg_price ap
JOIN
	avg_offer ao ON ap.model = ao.model
ORDER BY 1,2
	

SELECT 
	EXTRACT(YEAR FROM offer_date) AS year,
	EXTRACT(MONTH FROM offer_date) AS month
FROM offers
ORDER BY 1 , 2


-- Creating a window function for the average bid price of a brand and car model during the last 6 months.

WITH avg_offer_month AS(
	SELECT
		p.brand,
		p.model,
		EXTRACT(YEAR FROM o.offer_date) AS year,
		EXTRACT(MONTH FROM o.offer_date) AS month,
		ROUND(AVG(o.offer_price) OVER(PARTITION BY p.brand, p.model ORDER BY o.offer_date
									  ROWS BETWEEN 5 PRECEDING AND CURRENT ROW), 3) 
									  AS avg_offer_price
	FROM
		offers o
	JOIN
		advertisements a USING (advertisement_id)
	JOIN	
		products p USING (product_id)
	WHERE
		o.offer_date >= DATE '2023-07-01' AND o.offer_date < DATE '2024-01-01'
	ORDER BY 4 DESC
)
SELECT
	brand,
	model,
	MAX(CASE WHEN month = 7 THEN avg_offer_price END) AS avg_offer_july,
	MAX(CASE WHEN month = 8 THEN avg_offer_price END) AS avg_offer_august,
	MAX(CASE WHEN month = 9 THEN avg_offer_price END) AS avg_offer_september,
	MAX(CASE WHEN month = 10 THEN avg_offer_price END) AS avg_offer_october,
	MAX(CASE WHEN month = 11 THEN avg_offer_price END) AS avg_offer_november,
	MAX(CASE WHEN month = 12 THEN avg_offer_price END) AS avg_offer_december
FROM
	avg_offer_month
GROUP BY 1,2
ORDER BY 1,2
