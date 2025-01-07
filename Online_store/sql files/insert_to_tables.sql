INSERT INTO online_store.users (email, username, password, age, sex, faculty)
VALUES
('user1@example.com', 'user1', 'pass1234', 22, 0, 'Engineering'),
('user2@example.com', 'user2', 'pass1234', 25, 1, 'Mathematics'),
('user3@example.com', 'user3', 'pass1234', 21, 0, 'Chemistry'),
('user4@example.com', 'user4', 'pass1234', 24, 1, 'Statistics'),
('user5@example.com', 'user5', 'pass1234', 23, 0, 'Science'),
('user6@example.com', 'user6', 'pass1234', 26, 1, 'Engineering'),
('user7@example.com', 'user7', 'pass1234', 27, 0, 'Mathematics'),
('user8@example.com', 'user8', 'pass1234', 20, 1, 'Chemistry'),
('user9@example.com', 'user9', 'pass1234', 22, 0, 'Statistics'),
('user10@example.com', 'user10', 'pass1234', 28, 1, 'Science');

INSERT INTO online_store.managers (email, username, password, age, sex, faculty)
VALUES
('manager1@example.com', 'manager1', 'admin123', 35, 0, 'Engineering'),
('manager2@example.com', 'manager2', 'admin123', 40, 1, 'Mathematics'),
('manager3@example.com', 'manager3', 'admin123', 33, 0, 'Chemistry'),
('manager4@example.com', 'manager4', 'admin123', 38, 1, 'Statistics'),
('manager5@example.com', 'manager5', 'admin123', 36, 0, 'Science'),
('manager6@example.com', 'manager6', 'admin123', 45, 1, 'Engineering'),
('manager7@example.com', 'manager7', 'admin123', 50, 0, 'Mathematics'),
('manager8@example.com', 'manager8', 'admin123', 42, 1, 'Chemistry'),
('manager9@example.com', 'manager9', 'admin123', 37, 0, 'Statistics'),
('manager10@example.com', 'manager10', 'admin123', 48, 1, 'Science');


INSERT INTO online_store.clothes (cloth_id, cloth_name, price, available_amount, img_path)
VALUES
(16, 'Red T-Shirt', 20, 100, '/images/tshirt.jpg'),
(17, 'Jeans', 50, 80, '/images/jeans.jpg'),
(18, 'Jacket', 100, 50, '/images/jacket.jpg'),
(19, 'Sweater', 40, 70, '/images/sweater.jpg'),
(20, 'Shorts', 30, 60, '/images/shorts.jpg'),
(21, 'Skirt', 45, 90, '/images/skirt.jpg'),
(22, 'Dress', 75, 40, '/images/dress.jpg'),
(23, 'Black T-Shirt', 25, 85, '/images/black-T.jpg'),
(24, 'White T-Shirt', 25, 150, '/images/white-T.jpg'),
(25, 'Socks', 10, 200, '/images/socks.jpg'),
(26, 'Shoes', 120, 50, '/images/shoes.jpg'),
(27, 'Hat', 25, 100, '/images/hat.jpg'),
(28, 'Scarf', 20, 75, '/images/scarf.jpg'),
(29, 'Gloves', 18, 80, '/images/gloves.jpg'),
(30, 'Coat', 35, 110, '/images/coat.jpg');


INSERT INTO online_store.transactions (order_num, transaction_date, transaction_hour, email)
VALUES
(1001, '2024-01-01', '12:00:00', 'user1@example.com'),
(1002, '2024-01-02', '13:30:00', 'user2@example.com'),
(1003, '2024-01-03', '14:45:00', 'user3@example.com'),
(1004, '2024-01-04', '16:00:00', 'user4@example.com'),
(1005, '2024-01-05', '11:15:00', 'user5@example.com'),
(1006, '2024-01-06', '10:45:00', 'user6@example.com'),
(1007, '2024-01-07', '17:30:00', 'user7@example.com'),
(1008, '2024-01-08', '09:00:00', 'user8@example.com'),
(1009, '2024-01-09', '19:00:00', 'user9@example.com'),
(1010, '2024-01-10', '20:00:00', 'user10@example.com'),
(1011, '2024-01-11', '08:30:00', 'user1@example.com'),
(1012, '2024-01-12', '14:20:00', 'user2@example.com'),
(1013, '2024-01-13', '15:50:00', 'user3@example.com'),
(1014, '2024-01-14', '18:15:00', 'user4@example.com'),
(1015, '2024-01-15', '10:10:00', 'user5@example.com'),
(1016, '2024-01-16', '13:45:00', 'user6@example.com'),
(1017, '2024-01-17', '09:00:00', 'user7@example.com'),
(1018, '2024-01-18', '19:45:00', 'user8@example.com'),
(1019, '2024-01-19', '11:25:00', 'user9@example.com'),
(1020, '2024-01-20', '16:30:00', 'user10@example.com');

INSERT INTO online_store.clothes_in_transaction (order_num, cloth_id, amount)
VALUES
(1001, 1, 2),
(1002, 2, 1),
(1003, 3, 1),
(1004, 4, 3),
(1005, 5, 2),
(1006, 6, 1),
(1007, 7, 2),
(1008, 8, 1),
(1009, 9, 4),
(1010, 10, 3),
(1011, 11, 2),
(1012, 12, 1),
(1013, 13, 1),
(1014, 14, 3),
(1015, 15, 2),
(1016, 1, 1),
(1017, 3, 3),
(1018, 5, 2),
(1019, 7, 1),
(1020, 9, 4);


