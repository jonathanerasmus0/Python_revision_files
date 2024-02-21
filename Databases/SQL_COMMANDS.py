#SELECT

"""SELECT column1, column2
FROM table_name
WHERE condition;"""

#INSERT

"""INSERT INTO table_name (column1, column2)
VALUES (value1, value2);"""

#UPDATE table_name
"""SET column1 = value1, column2 = value2
WHERE condition;"""

#DELETE
"""DELETE FROM table_name
WHERE condition;"""

#CREATE
"""CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
"""
#DROP
"""ALTER TABLE table_name
ADD column_name datatype;"""

#CREATE INDEX
"""CREATE INDEX index_name
ON table_name (column_name);"""

#JOIN
"""SELECT column1, column2
FROM table1
INNER JOIN table2 ON table1.column = table2.column;"""

# GROUP BY
"""SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1;"""

#HAVING
"""SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1
HAVING COUNT(*) > 1;"""

#ORDER BY
"""SELECT column1, column2
FROM table_name
ORDER BY column1 DESC;"""

#WHERE
"""SELECT column1, column2
FROM table_name
WHERE column1 = value;"""

#UNION
"""SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;"""

#UNION ALL
"""SELECT column1 FROM table1
UNION ALL
SELECT column1 FROM table2;"""

#CREATE DATABASE
"""CREATE DATABASE database_name;"""

#DROP DATABASE
"""DROP DATABASE database_name;"""

#GRANT
"""DROP DATABASE database_name;"""

#REVOKE
"""REVOKE privilege_type
ON object_name
FROM user_name;"""

#















