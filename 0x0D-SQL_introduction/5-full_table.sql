-- Script to print the full description of the table first_table from the database hbtn_0c_0
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE TABLE_SCHEMA = '[database_name]'
AND TABLE_NAME = 'first_table';
