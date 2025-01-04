-- popularity report min
SELECT Distinct item_id, COUNT(item_num) AS amount
FROM temp_project.transaction
GROUP BY item_id
HAVING amount = (
    SELECT MIN(amount)
    FROM (
        SELECT COUNT(item_num) AS amount
        FROM temp_project.transaction
        GROUP BY item_id
    ) AS minimun_product
);
-- popularity report max
SELECT Distinct item_id, COUNT(item_num) AS amount
FROM temp_project.transaction
GROUP BY item_id
HAVING amount = (
    SELECT MAX(amount)
    FROM (
        SELECT COUNT(item_num) AS amount
        FROM temp_project.transaction
        GROUP BY item_id
    ) AS minimun_product
);
