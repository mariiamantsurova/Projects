CREATE SCHEMA IF NOT EXISTS online_store;


-- users
CREATE TABLE online_store.users(
email VARCHAR(45) NOT NULL UNIQUE,
username VARCHAR(45), 
password VARCHAR(10),
age INT,
sex boolean, # 0 male, 1 female 
faculty  VARCHAR(45),
is_admin boolean,
PRIMARY KEY(email)
);
-- transaction
CREATE TABLE online_store.transactions(
order_num INT NOT NULL UNIQUE,
date DATE, 
hour TIME, 
email VARCHAR(45), 
PRIMARY KEY(order_num),
FOREIGN KEY(email) REFERENCES users(email)
);

-- clothes
CREATE TABLE online_store.clothes(
sku INT NOT NULL UNIQUE,
name VARCHAR(45), 
price INT,
available_amount INT,
is_promoted BOOLEAN,
img_path VARCHAR(100),
PRIMARY KEY(sku)
);



-- clothes_in_transaction
CREATE TABLE online_store.clothes_in_transaction(
order_num INT NOT NULL,
sku INT NOT NULL,
amount INT,
PRIMARY KEY(order_num, sku),
FOREIGN KEY(order_num) REFERENCES transactions(order_num),
FOREIGN KEY(sku) REFERENCES clothes(sku)
);

CREATE TABLE online_store.new_items(
sku INT NOT NULL,
email VARCHAR(45) NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(sku, email, timestamp),
FOREIGN KEY(email) REFERENCES users(email),
FOREIGN KEY(sku) REFERENCES clothes(sku)
);

CREATE TABLE online_store.inventory_update(
sku INT NOT NULL,
email VARCHAR(45) NOT NULL,
quantity INT NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(sku, email, timestamp),
FOREIGN KEY(email) REFERENCES users(email),
FOREIGN KEY(sku) REFERENCES clothes(sku)
);

