
--Author: Lane Dorscher
--Date 12/20/2025

--Using the student table you created in Week 2, insert four rows into your table.
--Update the first name to “Luke” and last name to “Plew” for one of the rows you inserted above.
--Delete the row you updated above.

--CREATE SCHEMA BELLEVUE;
USE BELLEVUE;

--DROP TABLE STUDENT;

--CREATE TABLE STUDENT (
--	STUDENT_ID INT PRIMARY KEY,
--	STUDENT_FIRST_NAME VARCHAR(30) NOT NULL,
--	STUDENT_LAST_NAME VARCHAR(30) NOT NULL,
--	STUDENT_MIDDLE_NAME VARCHAR(30) NULL,
--	STUDENT_CITY VARCHAR(30) NOT NULL,
--	STUDENT_STATE VARCHAR(20) NOT NULL,
--	STUDENT_ZIP_CODE VARCHAR(14) NOT NULL,
--	STUDENT_GPA FLOAT NULL CHECK (STUDENT_GPA > 0.0 AND STUDENT_GPA <= 4.0)
--);

INSERT INTO STUDENT (
	STUDENT_ID,
	STUDENT_FIRST_NAME, 
	STUDENT_LAST_NAME, 
	STUDENT_MIDDLE_NAME, 
	STUDENT_CITY, 
	STUDENT_STATE, 
	STUDENT_ZIP_CODE, 
	STUDENT_GPA)
VALUES 
	(1, 'Lane', 'Dorscher', '', 'Council Bluffs', 'Iowa', '51503', 3.0),
	(2,'John', 'Doe', '', 'Omaha', 'Nebraska', '55555', 2.9),
	(3,'Morgan', 'L''Fay', '', 'Council Bluffs', 'Iowa', '51503', 4),
	(4,'Percy', 'De Rolo', 'Von', 'Out of ideas', 'Iowa', '78946', 3.0);

UPDATE STUDENT SET
	STUDENT_FIRST_NAME = 'Luke',
	STUDENT_LAST_NAME = 'Plew'
WHERE STUDENT_ID = 2;

SELECT * FROM STUDENT;
