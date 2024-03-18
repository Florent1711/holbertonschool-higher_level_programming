0-list_databases.sql - Write a script that lists all databases of your MySQL server.

1-create_database_if_missing.sql - Write a script that creates the database hbtn_0c_0 in your MySQL server.
    • If the database hbtn_0c_0 already exists, your script should not fail
    • You are not allowed to use the SELECT or SHOW statements

2-remove_database.sql - Write a script that deletes the database hbtn_0c_0 in your MySQL server.
    • If the database hbtn_0c_0 doesn’t exist, your script should not fail
    • You are not allowed to use the SELECT or SHOW statements

3-list_tables.sql - Write a script that lists all the tables of a database in your MySQL server.
    • The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

4-first_table.sql - Write a script that creates a table called first_table in the current database in your MySQL server.
    • first_table description:
        -id INT
        -name VARCHAR(256)
    • The database name will be passed as an argument of the mysql command
    • If the table first_table already exists, your script should not fail
    • You are not allowed to use the SELECT or SHOW statements

5-full_table.sql - Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
    • The database name will be passed as an argument of the mysql command
    • You are not allowed to use the DESCRIBE or EXPLAIN statements

6-list_values.sql - Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
    • All fields should be printed
    • The database name will be passed as an argument of the mysql command