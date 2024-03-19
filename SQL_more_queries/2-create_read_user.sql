-- creates the database hbtn_0d_2 and the user user_0d_2

-- Check if the database exists and create it if it does not
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user with the specified password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the new database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;