-- Prepares the MySQL server for this project
CREATE DATABASE IF NOT EXISTS California_dev_db;
CREATE USER IF NOT EXISTS 'California_dev'@'localhost' IDENTIFIED BY 'California_dev_pwd';
GRANT ALL PRIVILEGES ON `California_dev_db`.* TO 'California_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'California_dev'@'localhost';
FLUSH PRIVILEGES;
