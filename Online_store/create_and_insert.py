import mysql.connector

# ✅ Database connection settings
db_config = {
    "host": "localhost",  # Change if your MySQL is on another server
    "user": "root",       # Change to your MySQL username
    "password": "root", 
}

# ✅ Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# ✅ Create Schema
cursor.execute("CREATE SCHEMA IF NOT EXISTS online_store_15;")
cursor.execute("USE online_store_15;")

# ✅ Create Tables
tables = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(45) NOT NULL UNIQUE,
            username VARCHAR(45),
            password VARCHAR(10),
            age INT,
            sex BOOLEAN,  -- 0 = Male, 1 = Female
            faculty VARCHAR(45),
            is_admin BOOLEAN,
            PRIMARY KEY(email)
        );
    """,
    "transactions": """
        CREATE TABLE IF NOT EXISTS transactions (
            order_num INT NOT NULL UNIQUE,
            date DATE,
            hour TIME,
            email VARCHAR(45),
            PRIMARY KEY(order_num),
            FOREIGN KEY(email) REFERENCES users(email)
        );
    """,
    "clothes": """
        CREATE TABLE IF NOT EXISTS clothes (
            sku INT NOT NULL UNIQUE,
            name VARCHAR(45),
            price INT,
            available_amount INT,
            is_promoted BOOLEAN,
            img_path VARCHAR(100),
            PRIMARY KEY(sku)
        );
    """,
    "clothes_in_transaction": """
        CREATE TABLE IF NOT EXISTS clothes_in_transaction (
            order_num INT NOT NULL,
            sku INT NOT NULL,
            amount INT,
            PRIMARY KEY(order_num, sku),
            FOREIGN KEY(order_num) REFERENCES transactions(order_num),
            FOREIGN KEY(sku) REFERENCES clothes(sku)
        );
    """,
    "new_items": """
        CREATE TABLE IF NOT EXISTS new_items (
            sku INT NOT NULL,
            email VARCHAR(45) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(sku, email, timestamp),
            FOREIGN KEY(email) REFERENCES users(email),
            FOREIGN KEY(sku) REFERENCES clothes(sku)
        );
    """,
    "inventory_update": """
        CREATE TABLE IF NOT EXISTS inventory_update (
            sku INT NOT NULL,
            email VARCHAR(45) NOT NULL,
            quantity INT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(sku, email, timestamp),
            FOREIGN KEY(email) REFERENCES users(email),
            FOREIGN KEY(sku) REFERENCES clothes(sku)
        );
    """
}

# ✅ Execute table creation
for table_name, create_table_query in tables.items():
    cursor.execute(create_table_query)
    print(f"✅ Table '{table_name}' created successfully.")

# ✅ Insert Sample Data
sample_data = {
    "users": """
        INSERT INTO users (email, username, password, age, sex, faculty, is_admin)
        VALUES
        ('amelia.scott16@gmail.com', 'AmeliaScott16', '876543ab', 29, 1, 'Exact Sciences', 0),
        ('avery.lopez13@gmail.com', 'AveryLopez13', 'asdfgh12', 27, 0, 'Math', 0),
        ('benjamin.miller17@gmail.com', 'BenjaminMiller17', 'hello1234', 30, 0, 'Art', 0),
        ('charlotte.gonzalez14@gmail.com', 'CharlotteGonzalez14', 'ghijkl12', 24, 1, 'Engineering', 0),
        ('david.martinez5@gmail.com', 'DavidMartinez5', 'zxcvbn12', 26, 0, 'Art', 0),
        ('emily.davis4@gmail.com', 'EmilyDavis4', '98765432', 22, 1, 'Exact Sciences', 0),
        ('ethan.clark12@gmail.com', 'EthanClark12', 'lmnop987', 25, 1, 'Law', 0),
        ('harper.young18@gmail.com', 'HarperYoung18', 'pass9876', 22, 1, 'Law', 0),
        ('isabella.harris11@gmail.com', 'IsabellaHarris11', '98765zxc', 28, 0, 'Art', 0),
        ('jack.anderson15@gmail.com', 'JackAnderson15', '1sdf234k', 26, 0, 'Psychology', 0),
        ('james.wilson7@gmail.com', 'JamesWilson7', '12345abc', 27, 0, 'Math', 0),
        ('jane.smith2@gmail.com', 'JaneSmith2', 'qwerty12', 28, 1, 'Engineering', 0),
        ('john.doe1@gmail.com', 'JohnDoe1', 'pass1234', 25, 0, 'Math', 0),
        ('liam.moore9@gmail.com', 'LiamMoore9', 'abcdef12', 29, 0, 'Psychology', 0),
        ('lucas.allen19@gmail.com', 'LucasAllen19', 'abcde123', 23, 0, 'Math', 0),
        ('mason.taylor10@gmail.com', 'MasonTaylor10', '1qaz2wsx', 21, 1, 'Exact Sciences', 0),
        ('michael.brown3@gmail.com', 'MichaelBrown3', 'abc12345', 30, 0, 'Psychology', 0),
        ('mila.king20@gmail.com', 'MilaKing20', 'qwert098', 21, 1, 'Engineering', 0),
        ('miriam@example.com', 'miriam', 'pass456', 22, 1, 'Exact Sciences', 1),
        ('mishel@gmail.com', 'mishel', 'pass123', 25, 0, 'Exact Sciences', 1),
        ('naomi@example.com', 'naomi', 'pass456', 22, 1, 'Exact Sciences', 1),
        ('olivia.lee8@gmail.com', 'OliviaLee8', 'qwerty12', 23, 1, 'Engineering', 0),
        ('sophia.garcia6@gmail.com', 'SophiaGarcia6', 'passw1x2', 24, 1, 'Law', 0)
        ON DUPLICATE KEY UPDATE email=email;
    """,
    "transactions": """
        INSERT INTO transactions (order_num, date, hour, email)
        VALUES
        (1001, '2025-01-17', '14:30:00', 'john.doe1@gmail.com'),
        (1002, '2025-01-11', '15:10:45', 'john.doe1@gmail.com'),
        (1003, '2025-01-13', '16:45:55', 'john.doe1@gmail.com'),
        (1004, '2025-01-14', '17:21:12', 'john.doe1@gmail.com'),
        (1005, '2025-01-10', '14:33:21', 'john.doe1@gmail.com'),
        (1006, '2025-01-10', '15:12:02', 'jane.smith2@gmail.com'),
        (1007, '2025-01-12', '16:40:37', 'jane.smith2@gmail.com'),
        (1008, '2025-01-13', '18:53:55', 'jane.smith2@gmail.com'),
        (1009, '2025-01-18', '15:31:00', 'michael.brown3@gmail.com'),
        (1010, '2025-02-11', '16:45:00', 'michael.brown3@gmail.com'),
        (1011, '2025-01-10', '19:23:00', 'michael.brown3@gmail.com'),
        (1012, '2025-01-29', '16:00:00', 'emily.davis4@gmail.com'),
        (1013, '2025-01-11', '16:30:00', 'emily.davis4@gmail.com'),
        (1014, '2025-01-12', '17:15:21', 'emily.davis4@gmail.com'),
        (1015, '2025-01-13', '18:40:50', 'emily.davis4@gmail.com'),
        (1016, '2025-01-23', '16:30:00', 'david.martinez5@gmail.com'),
        (1017, '2025-01-10', '16:42:33', 'david.martinez5@gmail.com'),
        (1018, '2025-01-11', '17:07:18', 'david.martinez5@gmail.com'),
        (1019, '2025-01-12', '18:22:55', 'david.martinez5@gmail.com'),
        (1020, '2025-01-13', '19:38:17', 'david.martinez5@gmail.com'),
        (1021, '2025-01-14', '20:47:41', 'david.martinez5@gmail.com'),
        (1022, '2025-01-10', '17:15:00', 'sophia.garcia6@gmail.com'),
        (1023, '2025-01-11', '18:28:35', 'sophia.garcia6@gmail.com'),
        (1024, '2025-01-13', '19:17:48', 'sophia.garcia6@gmail.com'),
        (1025, '2025-01-10', '17:54:07', 'james.wilson7@gmail.com'),
        (1026, '2025-01-11', '19:12:03', 'james.wilson7@gmail.com'),
        (1027, '2025-01-12', '20:25:22', 'james.wilson7@gmail.com'),
        (1028, '2025-01-13', '21:33:47', 'james.wilson7@gmail.com'),
        (1029, '2025-01-18', '18:00:00', 'olivia.lee8@gmail.com'),
        (1030, '2025-01-26', '18:30:00', 'olivia.lee8@gmail.com'),
        (1031, '2025-01-11', '20:56:44', 'olivia.lee8@gmail.com'),
        (1032, '2025-01-10', '18:41:19', 'liam.moore9@gmail.com'),
        (1033, '2025-01-11', '21:12:54', 'liam.moore9@gmail.com'),
        (1034, '2025-01-12', '22:38:06', 'liam.moore9@gmail.com'),
        (1035, '2025-01-13', '23:55:28', 'liam.moore9@gmail.com'),
        (1036, '2025-01-14', '00:30:14', 'liam.moore9@gmail.com'),
        (1037, '2025-01-13', '14:30:00', 'mason.taylor10@gmail.com'),
        (1038, '2025-01-11', '15:28:00', 'mason.taylor10@gmail.com'),
        (1039, '2025-01-11', '15:30:00', 'mason.taylor10@gmail.com'),
        (1040, '2025-02-11', '16:45:00', 'mason.taylor10@gmail.com'),
        (1041, '2025-01-17', '14:35:00', 'john.doe1@gmail.com'),
        (1042, '2025-01-20', '16:00:00', 'john.doe1@gmail.com'),
        (1043, '2025-01-25', '18:10:00', 'john.doe1@gmail.com'),
        (1044, '2025-01-18', '15:00:00', 'jane.smith2@gmail.com'),
        (1045, '2025-01-21', '17:45:00', 'jane.smith2@gmail.com'),
        (1046, '2025-01-23', '19:10:00', 'jane.smith2@gmail.com'),
        (1047, '2025-01-28', '20:50:00', 'jane.smith2@gmail.com'),
        (1048, '2025-01-19', '14:00:00', 'michael.brown3@gmail.com'),
        (1049, '2025-01-22', '15:35:00', 'michael.brown3@gmail.com'),
        (1050, '2025-01-26', '17:55:00', 'michael.brown3@gmail.com'),
        (1051, '2025-01-17', '16:45:00', 'emily.davis4@gmail.com'),
        (1052, '2025-01-19', '18:00:00', 'emily.davis4@gmail.com'),
        (1053, '2025-01-24', '19:30:00', 'emily.davis4@gmail.com'),
        (1054, '2025-01-30', '21:00:00', 'emily.davis4@gmail.com'),
        (1055, '2025-01-18', '15:15:00', 'david.martinez5@gmail.com'),
        (1056, '2025-01-22', '16:30:00', 'david.martinez5@gmail.com'),
        (1057, '2025-01-26', '18:20:00', 'david.martinez5@gmail.com'),
        (1058, '2025-01-29', '20:40:00', 'david.martinez5@gmail.com'),
        (1059, '2025-01-17', '15:50:00', 'liam.moore9@gmail.com'),
        (1060, '2025-01-21', '17:15:00', 'liam.moore9@gmail.com'),
        (1061, '2025-01-24', '19:45:00', 'liam.moore9@gmail.com'),
        (1062, '2025-01-28', '20:25:00', 'liam.moore9@gmail.com'),
        (1063, '2025-01-31', '22:05:00', 'liam.moore9@gmail.com'),
        (1064, '2025-01-01', '20:15:00', 'emily.davis4@gmail.com'),
        (1065, '2025-01-01', '10:10:00', 'john.doe1@gmail.com'),
        (1066, '2025-01-02', '12:25:00', 'john.doe1@gmail.com'),
        (1067, '2025-01-05', '21:15:00', 'john.doe1@gmail.com'),
        (1068, '2025-01-07', '20:15:00', 'john.doe1@gmail.com'),
        (1069, '2025-01-10', '14:14:00', 'john.doe1@gmail.com'),
        (1070, '2025-01-09', '20:15:00', 'john.doe1@gmail.com'),
        (1071, '2025-01-01', '15:10:00', 'john.doe1@gmail.com'),
        (1072, '2025-01-03', '11:25:00', 'john.doe1@gmail.com'),
        (1073, '2025-01-04', '21:15:00', 'john.doe1@gmail.com'),
        (1074, '2025-01-05', '17:17:00', 'john.doe1@gmail.com'),
        (1075, '2025-01-06', '14:24:00', 'john.doe1@gmail.com'),
        (1076, '2025-01-07', '18:15:00', 'john.doe1@gmail.com')
        ON DUPLICATE KEY UPDATE order_num=order_num;
    """,
    "clothes": """
        INSERT INTO clothes (sku, name, price, available_amount, is_promoted, img_path)
        VALUES
        (10, 'Basic White T-Shirt', 15, 100, 0, 'https://xcdn.next.co.uk/COMMON/Items/Default/Default/ItemImages/AltItemShot/315x472/235459s2.jpg'),
        (11, 'Black Graphic T-Shirt', 20, 80, 1, 'https://m.media-amazon.com/images/I/71N30DW0zuL._AC_SY879_.jpg'),
        (12, 'Cotton Crew Neck T-Shirt', 18, 50, 0, 'https://m.media-amazon.com/images/I/61vqJXW3PUL._AC_SX679_.jpg'),
        (13, 'V-Neck T-Shirt', 17, 60, 1, 'https://m.media-amazon.com/images/I/71P2AXC65iL._AC_SX679_.jpg'),
        (14, 'Slim Fit Blue Jeans', 40, 120, 0, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZjV6VCxaorzk8zzFbgBf3rxvyUg2DZyqtfw&s'),
        (15, 'Black Skinny Jeans', 45, 70, 1, 'https://cherryla.com/cdn/shop/products/BlackJeanBack_2048x.jpg?v=1680865591'),
        (16, 'Light Wash Denim Jeans', 35, 90, 0, 'https://m.media-amazon.com/images/I/71VvmPutrBL._AC_SY879_.jpg'),
        (17, 'Straight Leg Jeans', 38, 65, 0, 'https://www.mytheresa.com/media/1094/1238/100/5a/P00997103.jpg'),
        (18, 'Classic Leather Jacket', 120, 40, 1, 'https://www.schottnyc.com/images/800x800/519_BLK_FNT_NEW1.jpg'),
        (19, 'Denim Jacket', 60, 55, 0, 'https://www.mytheresa.com/media/1094/1238/100/a8/P00580765.jpg'),
        (20, 'Puffer Jacket', 80, 30, 1, 'https://m.media-amazon.com/images/I/61P3PdkkMuL._AC_SY879_.jpg')
        ON DUPLICATE KEY UPDATE sku=sku;
    """,
    "clothes_in_transaction": """
        INSERT INTO clothes_in_transaction (order_num, sku, amount)
        VALUES
        (1001, 10, 2),
        (1001, 14, 1),
        (1002, 12, 3),
        (1002, 16, 2),
        (1003, 13, 1),
        (1003, 18, 1),
        (1004, 15, 2),
        (1004, 20, 1),
        (1005, 12, 1),
        (1005, 19, 2),
        (1006, 11, 1),
        (1006, 17, 1),
        (1007, 14, 1),
        (1007, 20, 3),
        (1008, 15, 2),
        (1008, 20, 2),
        (1009, 10, 1),
        (1009, 19, 1),
        (1010, 13, 1),
        (1010, 20, 1),
        (1017, 14, 1),
        (1017, 19, 2),
        (1018, 10, 3),
        (1028, 11, 1),
        (1036, 14, 1),
        (1045, 17, 2),
        (1054, 16, 1),
        (1057, 19, 2),
        (1058, 12, 1),
        (1058, 14, 1),
        (1060, 19, 2),
        (1061, 15, 1),
        (1062, 13, 2),
        (1063, 15, 2),
        (1065, 14, 1),
        (1066, 17, 2),
        (1067, 16, 1),
        (1068, 19, 4),
        (1069, 15, 3),
        (1070, 13, 2),
        (1071, 14, 6),
        (1072, 17, 5),
        (1073, 18, 6),
        (1074, 20, 4),
        (1075, 12, 4),
        (1076, 13, 5)
        ON DUPLICATE KEY UPDATE order_num=order_num, sku=sku;
    """,
    "new_items": """
        INSERT INTO new_items (sku, email, timestamp)
        VALUES
       (10, 'naomi@example.com', '2025-01-27 18:50:12'),
        (15, 'naomi@example.com', '2025-01-27 18:50:12')
        ON DUPLICATE KEY UPDATE sku=sku, email=email;
    """,
    "inventory_update": """
        INSERT INTO inventory_update (sku, email, quantity, timestamp)
        VALUES
        (10, 'naomi@example.com', 20, '2025-01-27 18:50:26'),
        (10, 'naomi@example.com', 20, '2025-01-28 18:44:29'),
        (20, 'naomi@example.com', 15, '2025-01-27 18:50:26'),
        (20, 'naomi@example.com', 15, '2025-01-28 18:44:29')
        ON DUPLICATE KEY UPDATE sku=sku, email=email;
    """
}

# ✅ Execute insert statements
for table_name, insert_query in sample_data.items():
    cursor.execute(insert_query)
    print(f"✅ Data inserted into '{table_name}' successfully.")

# ✅ Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("\n🎉 Database setup completed successfully!")