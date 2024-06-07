-- Script to list all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT * FROM mysql.db WHERE user IN ('user_0d_1', 'user_0d_2');
