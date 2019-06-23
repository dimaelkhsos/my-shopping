How to use: - (if not running docker image)

1. Click "Clone or download" green button and download zip archive of python-cart-master
2. Unzip the archive
3. Open Command Prompt
4. Type cd python-cart-master (or directory where you unzipped your archive)
5. Once in the python-cart-master, type py -3 -m venv venv
6. Type venv\Scripts\activate
7. You should see (venv) now
8. Type pip install -r requirements.txt to install the required modules
9. Type python app.py
# my-shopping
================================================================================

To run from docker-compose
docker-compose build .
docker-compose run

=================================================================================

# Database structure (SQLite)
CREATE TABLE "Cart" (
	`user_id`	INTEGER,
	`product_id`	INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `Users`(`user_id`),
	FOREIGN KEY(`product_id`) REFERENCES `Products`(`product_id`)
)

CREATE TABLE `Categories` (
	`category_id`	INTEGER,
	`category_name`	TEXT,
	PRIMARY KEY(`category_id`)
)

CREATE TABLE "Products" (
	`product_id`	INTEGER,
	`name`	TEXT,
	`price`	REAL,
	`description`	TEXT,
	`picture`	TEXT,
	`category_id`	INTEGER,
	PRIMARY KEY(`product_id`),
	FOREIGN KEY(`category_id`) REFERENCES `Categories`(`category_id`)
)

CREATE TABLE `Users` (
	`user_id`	INTEGER,
	`email`	TEXT,
	`password`	TEXT,
	`first_name`	TEXT,
	`last_name`	TEXT,
	`address`	TEXT,
	`city`	TEXT,
	`state`	TEXT,
	`zipcode`	TEXT,
	PRIMARY KEY(`user_id`)
)

