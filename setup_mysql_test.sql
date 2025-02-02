-- Check if the database hbnb_test_db exists, if not, create it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user hbnb_test with a password hbnb_test_pwd, if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to the user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';


FLUSH PRIVILEGES;
