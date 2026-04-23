--Author: Lane Dorscher
--Date: 2/8/2026

USE Bellevue;

-- Backup tables
SELECT * INTO MODEL_BKUP_02082026 FROM MODEL;
SELECT * INTO CHARTER_BKUP_02082026 FROM CHARTER;

-- Alter MODEL table
ALTER TABLE MODEL
ADD MOD_WAIT_CHG AS
(
    CASE 
        WHEN MOD_CODE = 'C-90A' THEN 100
        WHEN MOD_CODE = 'PA23-250' THEN 50
        WHEN MOD_CODE = 'PA31-350' THEN 75
        ELSE 0
    END
);

-- Alter CHARTER table

ALTER TABLE CHARTER ADD 
    CHAR_FLT_CHG_HR NUMERIC(10,2),
    CHAR_FLT_CHG NUMERIC(10,2),
    CHAR_TAX_CHG REAL,
    CHAR_TOT_CHG REAL;

-- Create a trigger to automatically perform calculations for any new or updated data (execute solo)
-- Had issues creating computed columns when the calculations rely on the other computed columns which is painfully not allowed.
CREATE OR ALTER TRIGGER trg_UpdateCharterCharges
ON CHARTER
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE c
    SET CHAR_FLT_CHG = c.CHAR_HOURS_FLOWN * c.CHAR_FLT_CHG_HR
    FROM CHARTER c
    INNER JOIN inserted i 
        ON c.CHAR_TRIP = i.CHAR_TRIP;

    UPDATE c
    SET CHAR_TAX_CHG = c.CHAR_FLT_CHG * 0.08
    FROM CHARTER c
    INNER JOIN inserted i 
        ON c.CHAR_TRIP = i.CHAR_TRIP;

    UPDATE c
    SET CHAR_TOT_CHG = c.CHAR_FLT_CHG + c.CHAR_TAX_CHG
    FROM CHARTER c
    INNER JOIN inserted i 
        ON c.CHAR_TRIP = i.CHAR_TRIP;
END

-- Supply with initial flat rate
UPDATE CHARTER SET CHAR_FLT_CHG_HR = 187;
-- trigger should have calculated columns

-- trigger test
SELECT * FROM CHARTER;
UPDATE CHARTER SET CHAR_FLT_CHG_HR = 133 WHERE CHAR_TRIP = 10001;
SELECT * FROM CHARTER;

