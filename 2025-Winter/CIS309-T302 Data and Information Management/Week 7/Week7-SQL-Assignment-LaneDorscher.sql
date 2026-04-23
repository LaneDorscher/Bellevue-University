--Author: Lane Dorscher
--Date: 2/8/2026

USE BELLEVUE;

-- 1. Using your student table, what is the average GPA for each state?
SELECT 
    STUDENT_STATE, 
    AVG(STUDENT_GPA) AS AVG_IN_STATE 
FROM STUDENT
GROUP BY STUDENT_STATE ORDER BY STUDENT_STATE ASC;

-- 2. Using your student table, what is the average GPA for students who are in Florida or New York?
SELECT 
    STUDENT_STATE, 
    AVG(STUDENT_GPA) AS AVERAGE_GPA 
FROM STUDENT
WHERE UPPER(STUDENT_STATE) IN ('FLORIDA', 'NEW YORK') 
GROUP BY STUDENT_STATE
UNION ALL
SELECT 
    'COMBINED', 
    AVG(STUDENT_GPA)  
FROM STUDENT
WHERE UPPER(STUDENT_STATE) IN ('FLORIDA', 'NEW YORK') 

-- 3. Using your student table, return the average GPA for each state with an average GPA greater than 3.
SELECT 
    STUDENT_STATE, 
    AVG(STUDENT_GPA) AS AVERAGE_GPA 
FROM STUDENT
WHERE STUDENT_GPA > 3 
GROUP BY STUDENT_STATE 

-- 4. Using your student table, how many students from each state have an average GPA less than 2?

SELECT 
    STUDENT_STATE, 
    COUNT(*) AS NUM_OF_STUDENTS 
FROM STUDENT
WHERE STUDENT_GPA < 2
GROUP BY STUDENT_STATE;

SELECT 
    STUDENT_STATE, 
    AVG(STUDENT_GPA) AS Avg_GPA
FROM STUDENT
GROUP BY STUDENT_STATE
HAVING AVG(STUDENT_GPA) < 2;
