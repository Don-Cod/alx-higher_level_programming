-- This script contains some SQL commands that lists the
-- number of records with the same score in the table
-- second_table in the hbtn_0c_0 of your MySQL server.

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC
