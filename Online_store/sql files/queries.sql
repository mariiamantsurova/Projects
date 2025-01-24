
-- popularity query 
(
    -- Top 10 Most Popular
    SELECT 'Top 10' AS category, c.sku, c.name, SUM(c.available_amount) AS amount
    FROM online_store.clothes c
    JOIN online_store.clothes_in_transaction cit ON cit.sku = c.sku
    GROUP BY c.sku, c.name
    ORDER BY amount DESC
    LIMIT 10
)
UNION ALL
(
    -- Bottom 10 Least Popular
    SELECT 'Bottom 10' AS category, c.sku, c.name, SUM(c.available_amount) AS amount
    FROM online_store.clothes c
    JOIN online_store.clothes_in_transaction cit ON cit.sku = c.sku
    GROUP BY c.sku, c.name
    ORDER BY amount ASC
    LIMIT 10
)
ORDER BY category ASC
;
-- report 3.2
-- costumers' behavioral purchase by categories
WITH most_frequent AS (SELECT CIT.sku
						FROM online_store.clothes_in_transaction AS CIT
                        GROUP BY CIT.sku
                        HAVING SUM(CIT.amount) > (SELECT AVG(total_amount)
													FROM (SELECT SUM(CIT.amount) AS total_amount
															FROM online_store.clothes_in_transaction AS CIT
                                                            GROUP BY CIT.sku
                                                            )
                                                            AS subquery))

SELECT users.faculty, users.age, users.sex,
        COUNT(DISTINCT(T.order_num)),
        AVG(CIT.amount * clothes.price) AS avg_spending,
		GROUP_CONCAT(clothes.name ORDER BY clothes.name ASC) AS most_frequent_items
FROM online_store.transactions T JOIN online_store.users ON users.email = T.email
	JOIN online_store.clothes_in_transaction CIT ON T.order_num = CIT.order_num
	JOIN online_store.clothes ON CIT.sku = clothes.sku
    LEFT JOIN most_frequent ON CIT.sku = most_frequent.sku
GROUP BY users.faculty, users.age, users.sex
ORDER BY users.faculty, users.age,users.sex
;


-- campaign impact 
SELECT 
	CASE 
        WHEN c.is_promoted = 1 THEN 'YES'
        ELSE 'NO'
    END AS is_promoted,
    SUM(cit.amount) AS total_sales_quantity,
    SUM(cit.amount * c.price) AS total_revenue,
    COUNT(DISTINCT c.sku) AS num_products,
    SUM(cit.amount) * 100.0 / (SELECT SUM(l.amount) FROM online_store.clothes_in_transaction l)  AS sales_percentage,
    SUM(cit.amount * c.price) * 100.0 / (SELECT SUM(r.amount * s.price) FROM online_store.clothes s 
    JOIN online_store.clothes_in_transaction r ON s.sku = r.sku) AS revenue_percentage
FROM 
    online_store.clothes c
JOIN 
    online_store.clothes_in_transaction cit ON c.sku = cit.sku
GROUP BY 
    c.is_promoted;

-- inventory 
SELECT c.name , c.sku, c.available_amount FROM online_store.clothes c;

-- purchase report
SELECT u.username , t.date, t.hour , c.sku , c.name
FROM online_store.transactions t JOIN online_store.users u ON u.email = t.email 
JOIN online_store.clothes_in_transaction cit ON t.order_num = cit.order_num 
JOIN online_store.clothes c ON c.sku = cit.sku;


-- queries for visualizations:
-- most popular items per gender
SELECT users.sex, CIT.sku,  clothes.name ,COUNT(CIT.sku) AS num_purchases
FROM online_store.transactions T
JOIN online_store.users
ON users.email = T.email
JOIN online_store.clothes_in_transaction CIT
ON T.order_num = CIT.order_num
JOIN online_store.clothes
ON CIT.sku = clothes.sku
GROUP BY users.sex, CIT.sku
HAVING users.sex = 0
ORDER BY users.sex, num_purchases DESC;

-- number of items per gender
SELECT users.sex, SUM(CIT.amount) AS total_items_num
FROM online_store.transactions T
JOIN online_store.users
ON users.email = T.email
JOIN online_store.clothes_in_transaction CIT
ON T.order_num = CIT.order_num
JOIN online_store.clothes
ON CIT.sku = clothes.sku
GROUP BY users.sex
ORDER BY users.sex;

-- avg num of items per gender (per client)
SELECT users.sex, AVG(CIT.amount) AS avg_items_num
FROM online_store.transactions T
JOIN online_store.users
ON users.email = T.email
JOIN online_store.clothes_in_transaction CIT
ON T.order_num = CIT.order_num
JOIN online_store.clothes
ON CIT.sku = clothes.sku
GROUP BY users.sex
ORDER BY users.sex;
