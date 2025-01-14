
-- popularity query 
(
    -- Top 10 Most Popular
    SELECT 'Top 10' AS category, c.sku, c.name, SUM(t.amount) AS amount
    FROM online_store.clothes c
    JOIN online_store.clothes_in_transaction cit ON cit.sku = t.sku
    GROUP BY c.sku, c.name
    ORDER BY amount DESC
    LIMIT 10
)
UNION ALL
(
    -- Bottom 10 Least Popular
    SELECT 'Bottom 10' AS category, c.sku, c.name, SUM(t.amount) AS amount
    FROM online_store.clothes c
    JOIN online_store.clothes_in_transaction cit ON cit.sku = t.sku
    GROUP BY c.sku, c.name
    ORDER BY amount ASC
    LIMIT 10
)
ORDER BY category ASC;

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


