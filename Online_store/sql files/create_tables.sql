-- drop schema online_store;
-- drop TABLE temp_project.transaction;

CREATE SCHEMA IF NOT EXISTS online_store;

-- transaction
CREATE TABLE online_store.transactions(
order_num INT NOT NULL UNIQUE,
transaction_date DATE, 
transaction_hour TIME, 
email VARCHAR(45), 
PRIMARY KEY(order_num),
FOREIGN KEY(email) REFERENCES users(email)
);

-- clothes
CREATE TABLE online_store.clothes(
cloth_id INT NOT NULL UNIQUE,
cloth_name VARCHAR(45), 
price INT,
available_amount INT,
img_path VARCHAR(100),
PRIMARY KEY(cloth_id)
);

-- users
CREATE TABLE online_store.users(
email VARCHAR(45) NOT NULL UNIQUE,
username VARCHAR(45), 
password VARCHAR(10),
age INT,
sex boolean, # 0 male, 1 female 
faculty  VARCHAR(45),
PRIMARY KEY(email)
);

-- managers
CREATE TABLE online_store.managers(
email VARCHAR(45) NOT NULL UNIQUE,
username VARCHAR(45), 
password VARCHAR(10),
age INT,
sex boolean, # 0 male, 1 female 
faculty  VARCHAR(45),
PRIMARY KEY(email)
);

-- clothes_in_transaction
CREATE TABLE online_store.clothes_in_transaction(
order_num INT NOT NULL UNIQUE,
cloth_id INT NOT NULL UNIQUE,
amount INT,
PRIMARY KEY(order_num, cloth_id),
FOREIGN KEY(order_num) REFERENCES transactions(order_num),
FOREIGN KEY(cloth_id) REFERENCES clothes(cloth_id)
);

CREATE TABLE online_store.new_items(
cloth_id INT NOT NULL UNIQUE,
email VARCHAR(45) NOT NULL UNIQUE,
adding_date DATE NOT NULL,
adding_hour TIME NOT NULL
PRIMARY KEY(cloth_id, email, adding_date, adding_hour)
FOREIGN KEY(email) REFERENCES users(email),
FOREIGN KEY(cloth_id) REFERENCES clothes(cloth_id)
);

CREATE TABLE online_store.inventory_update(
cloth_id INT NOT NULL UNIQUE,
email VARCHAR(45) NOT NULL UNIQUE,
quantity INT NOT NULL,
update_date DATE NOT NULL,
update_hour TIME NOT NULL,
PRIMARY KEY(cloth_id, email, update_date, update_hour),
FOREIGN KEY(email) REFERENCES users(email),
FOREIGN KEY(cloth_id) REFERENCES clothes(cloth_id)
);

