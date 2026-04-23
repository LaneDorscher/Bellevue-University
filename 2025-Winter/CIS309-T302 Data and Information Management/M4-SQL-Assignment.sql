
--Author: Lane Dorscher
--Date 01/24/2025

--Before you start developing your SQL, review the following video: Homework SQL.
--    Using your student table, select all students that have a last name of “Parker” and have a first name that starts with “S”. 
--          Order your results by state.
--    Using your student table, select all students with ZIP codes between “23164” and “98164”.
--    Using your student table, select all students from the states of Florida and New York.
--    Using your student table, select all students whose last names start with an “S” and are at least three characters in length.

USE BELLEVUE;

SELECT * FROM STUDENT WHERE STUDENT_LAST_NAME = 'Parker' AND STUDENT_FIRST_NAME LIKE 'S%';
SELECT * FROM STUDENT WHERE STUDENT_ZIP_CODE > 23164 AND STUDENT_ZIP_CODE < 98164;
SELECT * FROM STUDENT WHERE UPPER(STUDENT_STATE) IN ('FL', 'FLORIDA', 'NY', 'NEW YORK');
--SELECT * FROM STUDENT WHERE UPPER(STUDENT_STATE) IN ('FL', 'FLORIDA', 'NE', 'NEBRASKA'); --ideally, entries would follow strict guidelines either using abbreviations or spelt out state names..
SELECT * FROM STUDENT WHERE STUDENT_LAST_NAME LIKE 'S%' AND LEN(STUDENT_LAST_NAME) >= 3;





