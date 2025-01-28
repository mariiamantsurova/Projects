-- Insert into users
INSERT INTO online_store.users (email, username, password, age, sex, faculty, is_admin)
VALUES 
('mishel@gmail.com', 'mishel', 'pass123', 25, 0, 'Exact Sciences', TRUE),
('miriam@example.com', 'miriam', 'pass456', 22, 1, 'Exact Sciences', TRUE),
('naomi@example.com', 'naomi', 'pass456', 22, 1, 'Exact Sciences', TRUE),
('john.doe1@gmail.com', 'JohnDoe1', 'pass1234', 25, 0, 'Math', FALSE),
('jane.smith2@gmail.com', 'JaneSmith2', 'qwerty12', 28, 1, 'Engineering', FALSE),
('michael.brown3@gmail.com', 'MichaelBrown3', 'abc12345', 30, 0, 'Psychology', FALSE),
('emily.davis4@gmail.com', 'EmilyDavis4', '98765432', 22, 1, 'Exact Sciences', FALSE),
('david.martinez5@gmail.com', 'DavidMartinez5', 'zxcvbn12', 26, 0, 'Art', FALSE),
('sophia.garcia6@gmail.com', 'SophiaGarcia6', 'passw1x2', 24, 1, 'Law', FALSE),
('james.wilson7@gmail.com', 'JamesWilson7', '12345abc', 27, 0, 'Math', FALSE),
('olivia.lee8@gmail.com', 'OliviaLee8', 'qwerty12', 23, 1, 'Engineering', FALSE),
('liam.moore9@gmail.com', 'LiamMoore9', 'abcdef12', 29, 0, 'Psychology', FALSE),
('mason.taylor10@gmail.com', 'MasonTaylor10', '1qaz2wsx', 21, 1, 'Exact Sciences', FALSE),
('isabella.harris11@gmail.com', 'IsabellaHarris11', '98765zxc', 28, 0, 'Art', FALSE),
('ethan.clark12@gmail.com', 'EthanClark12', 'lmnop987', 25, 1, 'Law', FALSE),
('avery.lopez13@gmail.com', 'AveryLopez13', 'asdfgh12', 27, 0, 'Math', FALSE),
('charlotte.gonzalez14@gmail.com', 'CharlotteGonzalez14', 'ghijkl12', 24, 1, 'Engineering', FALSE),
('jack.anderson15@gmail.com', 'JackAnderson15', '1sdf234k', 26, 0, 'Psychology', FALSE),
('amelia.scott16@gmail.com', 'AmeliaScott16', '876543ab', 29, 1, 'Exact Sciences', FALSE),
('benjamin.miller17@gmail.com', 'BenjaminMiller17', 'hello1234', 30, 0, 'Art', FALSE),
('harper.young18@gmail.com', 'HarperYoung18', 'pass9876', 22, 1, 'Law', FALSE),
('lucas.allen19@gmail.com', 'LucasAllen19', 'abcde123', 23, 0, 'Math', FALSE),
('mila.king20@gmail.com', 'MilaKing20', 'qwert098', 21, 1, 'Engineering', FALSE);

-- Insert into transactions
-- Transactions for users, with unique order_num values:

-- John Doe (john.doe1@gmail.com) - 5 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1001, '2025-01-17', '14:30:00', 'john.doe1@gmail.com'),
(1002, '2025-01-11', '15:10:45', 'john.doe1@gmail.com'),
(1003, '2025-01-13', '16:45:55', 'john.doe1@gmail.com'),
(1004, '2025-01-14', '17:21:12', 'john.doe1@gmail.com'),
(1005, '2025-01-10', '14:33:21', 'john.doe1@gmail.com');

-- Jane Smith (jane.smith2@gmail.com) - 3 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1006, '2025-01-10', '15:12:02', 'jane.smith2@gmail.com'),
(1007, '2025-01-12', '16:40:37', 'jane.smith2@gmail.com'),
(1008, '2025-01-13', '18:53:55', 'jane.smith2@gmail.com');

-- Michael Brown (michael.brown3@gmail.com) - 3 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1009, '2025-01-18', '15:31:00', 'michael.brown3@gmail.com'),
(1010, '2025-02-11', '16:45:00', 'michael.brown3@gmail.com'),
(1011, '2025-01-10', '19:23:00', 'michael.brown3@gmail.com');

-- Emily Davis (emily.davis4@gmail.com) - 4 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1012, '2025-01-29', '16:00:00', 'emily.davis4@gmail.com'),
(1013, '2025-01-11', '16:30:00', 'emily.davis4@gmail.com'),
(1014, '2025-01-12', '17:15:21', 'emily.davis4@gmail.com'),
(1015, '2025-01-13', '18:40:50', 'emily.davis4@gmail.com');

-- David Martinez (david.martinez5@gmail.com) - 6 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1016, '2025-01-23', '16:30:00', 'david.martinez5@gmail.com'),
(1017, '2025-01-10', '16:42:33', 'david.martinez5@gmail.com'),
(1018, '2025-01-11', '17:07:18', 'david.martinez5@gmail.com'),
(1019, '2025-01-12', '18:22:55', 'david.martinez5@gmail.com'),
(1020, '2025-01-13', '19:38:17', 'david.martinez5@gmail.com'),
(1021, '2025-01-14', '20:47:41', 'david.martinez5@gmail.com');

-- Sophia Garcia (sophia.garcia6@gmail.com) - 3 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1022, '2025-01-10', '17:15:00', 'sophia.garcia6@gmail.com'),
(1023, '2025-01-11', '18:28:35', 'sophia.garcia6@gmail.com'),
(1024, '2025-01-13', '19:17:48', 'sophia.garcia6@gmail.com');

-- James Wilson (james.wilson7@gmail.com) - 4 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1025, '2025-01-10', '17:54:07', 'james.wilson7@gmail.com'),
(1026, '2025-01-11', '19:12:03', 'james.wilson7@gmail.com'),
(1027, '2025-01-12', '20:25:22', 'james.wilson7@gmail.com'),
(1028, '2025-01-13', '21:33:47', 'james.wilson7@gmail.com');

-- Olivia Lee (olivia.lee8@gmail.com) - 3 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1029, '2025-01-18', '18:00:00', 'olivia.lee8@gmail.com'),
(1030, '2025-01-26', '18:30:00', 'olivia.lee8@gmail.com'),
(1031, '2025-01-11', '20:56:44', 'olivia.lee8@gmail.com');

-- Liam Moore (liam.moore9@gmail.com) - 5 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1032, '2025-01-10', '18:41:19', 'liam.moore9@gmail.com'),
(1033, '2025-01-11', '21:12:54', 'liam.moore9@gmail.com'),
(1034, '2025-01-12', '22:38:06', 'liam.moore9@gmail.com'),
(1035, '2025-01-13', '23:55:28', 'liam.moore9@gmail.com'),
(1036, '2025-01-14', '00:30:14', 'liam.moore9@gmail.com');

-- Mason Taylor (mason.taylor10@gmail.com) - 4 transactions
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1037, '2025-01-13', '14:30:00', 'mason.taylor10@gmail.com'),
(1038, '2025-01-11', '15:28:00', 'mason.taylor10@gmail.com'),
(1039, '2025-01-11', '15:30:00', 'mason.taylor10@gmail.com'),
(1040, '2025-02-11', '16:45:00', 'mason.taylor10@gmail.com');

-- John Doe
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1041, '2025-01-17', '14:35:00', 'john.doe1@gmail.com'),
(1042, '2025-01-20', '16:00:00', 'john.doe1@gmail.com'),
(1043, '2025-01-25', '18:10:00', 'john.doe1@gmail.com');

-- Jane Smith
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1044, '2025-01-18', '15:00:00', 'jane.smith2@gmail.com'),
(1045, '2025-01-21', '17:45:00', 'jane.smith2@gmail.com'),
(1046, '2025-01-23', '19:10:00', 'jane.smith2@gmail.com'),
(1047, '2025-01-28', '20:50:00', 'jane.smith2@gmail.com');

-- Michael Brown
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1048, '2025-01-19', '14:00:00', 'michael.brown3@gmail.com'),
(1049, '2025-01-22', '15:35:00', 'michael.brown3@gmail.com'),
(1050, '2025-01-26', '17:55:00', 'michael.brown3@gmail.com');

-- Emily Davis
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1051, '2025-01-17', '16:45:00', 'emily.davis4@gmail.com'),
(1052, '2025-01-19', '18:00:00', 'emily.davis4@gmail.com'),
(1053, '2025-01-24', '19:30:00', 'emily.davis4@gmail.com'),
(1054, '2025-01-30', '21:00:00', 'emily.davis4@gmail.com');

-- David Martinez
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1055, '2025-01-18', '15:15:00', 'david.martinez5@gmail.com'),
(1056, '2025-01-22', '16:30:00', 'david.martinez5@gmail.com'),
(1057, '2025-01-26', '18:20:00', 'david.martinez5@gmail.com'),
(1058, '2025-01-29', '20:40:00', 'david.martinez5@gmail.com');

-- Liam Moore
INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES
(1059, '2025-01-17', '15:50:00', 'liam.moore9@gmail.com'),
(1060, '2025-01-21', '17:15:00', 'liam.moore9@gmail.com'),
(1061, '2025-01-24', '19:45:00', 'liam.moore9@gmail.com'),
(1062, '2025-01-28', '20:25:00', 'liam.moore9@gmail.com'),
(1063, '2025-01-31', '22:05:00', 'liam.moore9@gmail.com');




-- Insert into clothes
INSERT INTO online_store.clothes (sku, name, price, available_amount, is_promoted, img_path)
VALUES
(10, 'Basic White T-Shirt', 15, 100, FALSE, 'https://xcdn.next.co.uk/COMMON/Items/Default/Default/ItemImages/AltItemShot/315x472/235459s2.jpg'),
(11, 'Black T-Shirt', 20, 80, TRUE, 'https://vibez-store.com/wp-content/uploads/2024/11/tshirt-1.jpg'),
(12, 'Sweater', 18, 50, FALSE, 'https://m.media-amazon.com/images/I/61DIDk2kiML._AC_SX679_.jpg'),
(13, 'V-Neck T-Shirt', 17, 60, TRUE, 'https://m.media-amazon.com/images/I/61vqJXW3PUL._AC_SX679_.jpg'),
(14, 'Slim Fit Blue Jeans', 40, 120, FALSE, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZjV6VCxaorzk8zzFbgBf3rxvyUg2DZyqtfw&s'),
(15, 'Black Skinny Jeans', 45, 70, TRUE, 'https://cherryla.com/cdn/shop/products/BlackJeanBack_2048x.jpg?v=1680865591'),
(16, 'Dress', 35, 90, FALSE, 'https://m.media-amazon.com/images/I/51ywkd-yHpL._AC_.jpg'),
(17, 'Jacket', 38, 65, FALSE, 'https://cdn-images.farfetch-contents.com/24/09/94/78/24099478_54252248_600.jpg'),
(18, 'Classic Leather Jacket', 120, 40, TRUE, 'https://www.schottnyc.com/images/800x800/519_BLK_FNT_NEW1.jpg'),
(19, 'Denim Jacket', 60, 55, FALSE, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNxGUDHFbfV86N7mSE97jxm8r-FPioPEhVww&s'),
(20, 'Puffer Jacket', 80, 30, TRUE, 'https://m.media-amazon.com/images/I/61P3PdkkMuL._AC_SY879_.jpg');


-- Insert into clothes_in_transaction
INSERT INTO online_store.clothes_in_transaction (order_num, sku, amount) VALUES
(1001, 10, 2),  -- Order 1001, Basic White T-Shirt, 2 pieces
(1001, 14, 1),  -- Order 1001, Slim Fit Blue Jeans, 1 piece
(1002, 12, 3),  -- Order 1002, Cotton Crew Neck T-Shirt, 3 pieces
(1002, 16, 2),  -- Order 1002, Light Wash Denim Jeans, 2 pieces
(1003, 13, 1),  -- Order 1003, V-Neck T-Shirt, 1 piece
(1003, 18, 1),  -- Order 1003, Classic Leather Jacket, 1 piece
(1004, 20, 1),  -- Order 1004, Puffer Jacket, 1 piece
(1004, 15, 2),  -- Order 1004, Black Skinny Jeans, 2 pieces
(1005, 12, 1),  -- Order 1005, Cashmere Sweater, 1 piece
(1005, 19, 2),  -- Order 1005, Running Sneakers, 2 pieces
(1006, 11, 1),  -- Order 1006, Black Graphic T-Shirt, 1 piece
(1006, 17, 1),  -- Order 1006, Straight Leg Jeans, 1 piece
(1007, 20, 3),  -- Order 1007, Crew Neck Sweater, 3 pieces
(1007, 14, 1),  -- Order 1007, Slim Fit Blue Jeans, 1 piece
(1008, 20, 2),  -- Order 1008, Fleece Hoodie, 2 pieces
(1008, 15, 2),  -- Order 1008, Black Skinny Jeans, 2 pieces
(1009, 10, 1),  -- Order 1009, Basic White T-Shirt, 1 piece
(1009, 19, 1),  -- Order 1009, Denim Jacket, 1 piece
(1010, 13, 1),  -- Order 1010, V-Neck T-Shirt, 1 piece
(1010, 20, 1);  -- Order 1010, Running Sneakers, 1 piece Order 1010, Running Sneakers, 1 piece


-- Insert into new_items
INSERT INTO online_store.new_items (sku, email)
VALUES
(10, 'naomi@example.com'), -- Admin adds T-Shirt
(15, 'naomi@example.com'); -- Admin adds Jeans

-- Insert into inventory_update
INSERT INTO online_store.inventory_update (sku, email, quantity)
VALUES
(10, 'naomi@example.com', 20), -- Admin updates inventory for T-Shirt
(20, 'naomi@example.com', 15); -- Admin updates inventory for Jeans