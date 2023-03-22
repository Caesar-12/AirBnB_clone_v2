-- Prepareas mysql server for project

CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXIST 'hbnb_test'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';