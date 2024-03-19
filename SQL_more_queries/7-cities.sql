-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)

-- Check if the database exist and create it if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the Database to use
USE hbtn_0d_usa;

-- Check if the table exist and create it if not
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO-INCREMENT,
    state_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
