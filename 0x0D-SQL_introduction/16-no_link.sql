-- This script contains some SQL commands that lists all
-- the records of the second_table of the hbtn_0c_0 database
-- of your MySQL server.

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
