-- Prepares the MySQL server for this project
CREATE DATABASE IF NOT EXISTS California_test_db;
CREATE USER IF NOT EXISTS 'California_test'@'localhost' IDENTIFIED BY 'California_test_pwd';
GRANT ALL PRIVILEGES ON `California_test_db`.* TO 'California_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'California_test'@'localhost';
FLUSH PRIVILEGES;
