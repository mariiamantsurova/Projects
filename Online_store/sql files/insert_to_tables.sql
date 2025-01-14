-- Insert into users
INSERT INTO online_store.users (email, username, password, age, sex, faculty, is_admin)
VALUES 
('john.doe@example.com', 'johndoe', 'pass123', 25, 0, 'Engineering', FALSE),
('jane.doe@example.com', 'janedoe', 'pass456', 22, 1, 'Medicine', FALSE),
('admin@store.com', 'adminuser', 'admin789', 30, 0, 'Management', TRUE);

-- Insert into transactions
INSERT INTO online_store.transactions (order_num, date, hour, email)
VALUES
(1001, '2025-01-10', '14:30:00', 'john.doe@example.com'),
(1002, '2025-01-11', '15:00:00', 'jane.doe@example.com');

-- Insert into clothes
INSERT INTO online_store.clothes (sku, name, price, available_amount, is_promoted, img_path)
VALUES
(101, 'T-Shirt', 25, 50, TRUE, '/images/tshirt.jpg'),
(102, 'Jeans', 40, 30, FALSE, '/images/jeans.jpg'),
(103, 'Jacket', 60, 20, TRUE, '/images/jacket.jpg');

-- Insert into clothes_in_transaction
INSERT INTO online_store.clothes_in_transaction (order_num, sku, amount)
VALUES
(1001, 101, 2), -- 2 T-Shirts in John's order
(1002, 103, 1); -- 1 Jacket in Jane's orde


-- Insert into new_items
INSERT INTO online_store.new_items (sku, email)
VALUES
(101, 'admin@store.com'), -- Admin adds T-Shirt
(102, 'admin@store.com'); -- Admin adds Jeans

-- Insert into inventory_update
INSERT INTO online_store.inventory_update (sku, email, quantity)
VALUES
(101, 'admin@store.com', 20), -- Admin updates inventory for T-Shirt
(102, 'admin@store.com', 15); -- Admin updates inventory for Jeans