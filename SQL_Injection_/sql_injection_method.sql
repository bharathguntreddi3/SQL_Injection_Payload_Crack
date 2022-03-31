SELECT * FROM sql_injection WHERE username = 1223455 OR 1=1

-- An attacker can place the malicious code in SQL statements, via web page input 


-- Attacker enter 122345 OR 1=1 is always true into the web page input 
-- Since its true for all the attacker might get access to all usernames and password in a database .
-- And can also access the valuable information in the databases and can alter or delete data 


SELECT * FROM Users WHERE username ="" or ""="" AND password ="" or ""=""

-- If you enter username and password as  " or ""="  will result above query
-- " or ""=" query is valid and returns all rows from tables since it is always true

SELECT * FROM sql_injection; DROP TABLE sql_injection;
-- Will select and drops the table sql_injection

