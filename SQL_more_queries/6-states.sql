-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)

-- Check if the database exists and create it if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to use
USE hbtn_0d_usa;

-- Check if the table exist and create it if not
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
