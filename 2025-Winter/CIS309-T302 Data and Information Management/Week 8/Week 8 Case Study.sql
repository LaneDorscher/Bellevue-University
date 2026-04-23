-- Author: Lane Dorscher
-- Date: 2/15/2025

-- CUSTOMER
CREATE TABLE CUSTOMER (
    CUSTOMER_ID INT PRIMARY KEY,
    CUSTOMER_F_NAME VARCHAR(30),
    CUSTOMER_M_NAME VARCHAR(30),
    CUSTOMER_L_NAME VARCHAR(30),
    CUSTOMER_STREET_ADDRESS VARCHAR(150),
    CUSTOMER_CITY VARCHAR(50),
    CUSTOMER_STATE VARCHAR(30),
    CUSTOMER_ZIP_CODE VARCHAR(14),
    CUSTOMER_PHONE VARCHAR(12)
);

-- SUPPLIER
CREATE TABLE SUPPLIER (
    SUPPLIER_ID INT PRIMARY KEY,
    SUPPLIER_NAME VARCHAR(100),
    SUPPLIER_CONTACT_NAME VARCHAR(100),
    SUPPLIER_CONTACT_PHONE VARCHAR(12),
    SUPPLIER_CREDIT_TERM_DAYS INT
);

-- PROJECT
CREATE TABLE PROJECT (
    PROJECT_ID INT PRIMARY KEY,
    CUSTOMER_ID INT,
    PROJECT_STREET_ADDRESS VARCHAR(150),
    PROJECT_CITY VARCHAR(50),
    PROJECT_STATE VARCHAR(30),
    PROJECT_ZIP_CODE VARCHAR(14),
    PROJECT_START_DATE DATETIME,
    PROJECT_END_DATE DATETIME,
    PROJECT_STATUS VARCHAR(15),
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID)
);

-- BID
CREATE TABLE BID (
    BID_ID INT PRIMARY KEY,
    PROJECT_ID INT,
    BID_DATE DATETIME,
    BID_ESTIMATED_HOURS INT,
    BID_LABOR_RATE FLOAT,
    BID_ESTIMATED_MATERIAL_COST FLOAT,
    BID_ESTIMATED_COST FLOAT,
    BID_STATUS VARCHAR(15),
    FOREIGN KEY (PROJECT_ID) REFERENCES PROJECT(PROJECT_ID)
);

-- REPAIR
CREATE TABLE REPAIR (
    REPAIR_ID INT PRIMARY KEY,
    BID_ID INT,
    REPAIR_DESCRIPTION VARCHAR(255),
    REPAIR_HOURS_WORKED INT,
    REPAIR_LABOR_COST FLOAT,
    FOREIGN KEY (BID_ID) REFERENCES BID(BID_ID)
);

-- MATERIAL
CREATE TABLE MATERIAL (
    MATERIAL_ID INT PRIMARY KEY,
    SUPPLIER_ID INT,
    MATERIAL_NAME VARCHAR(100),
    MATERIAL_DESCRIPTION VARCHAR(255),
    UNIT_TYPE VARCHAR(25),
    UNIT_COST FLOAT,
    FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID)
);

-- REPAIR_MATERIAL
CREATE TABLE REPAIR_MATERIAL (
    MATERIAL_ID INT,
    REPAIR_ID INT,
    QUANTITY_USED INT,
    EXTENDED_COST FLOAT,
    PRIMARY KEY (MATERIAL_ID, REPAIR_ID),
    FOREIGN KEY (MATERIAL_ID) REFERENCES MATERIAL(MATERIAL_ID),
    FOREIGN KEY (REPAIR_ID) REFERENCES REPAIR(REPAIR_ID)
);

-- SUPPLIER_PAYMENT
CREATE TABLE SUPPLIER_PAYMENT (
    SUPPLIER_PAYMENT_ID INT PRIMARY KEY,
    SUPPLIER_ID INT,
    PAYMENT_DATE DATE,
    PAYMENT_AMOUNT FLOAT,
    PAYMENT_METHOD VARCHAR(20),
    FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID)
);

-- CUSTOMER_PAYMENT
CREATE TABLE CUSTOMER_PAYMENT (
    CUSTOMER_PAYMENT_ID INT PRIMARY KEY,
    CUSTOMER_ID INT,
    PROJECT_ID INT,
    PAYMENT_DATE DATE,
    PAYMENT_AMOUNT FLOAT,
    PAYMENT_METHOD VARCHAR(20),
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
    FOREIGN KEY (PROJECT_ID) REFERENCES PROJECT(PROJECT_ID)
);


-- Sample Data

INSERT INTO CUSTOMER VALUES
(1, 'Lane', 'M', 'Dorscher', '123 Maple Street', 'Omaha', 'NE', '68164', '4025551001'),
(2, 'Peter', NULL, 'Parker', '20 Ingram Street', 'Queens', 'NY', '11375', '2125552002'),
(3, 'John', NULL, 'Shepard', '742 Evergreen Terrace', 'Springfield', 'IL', '62701', '2175553003'),
(4, 'Garrus', NULL, 'Vakarian', '456 Oak Avenue', 'Seattle', 'WA', '98101', '2065554004'),
(5, 'Tali', NULL, 'Zorah', '789 Pine Drive', 'San Diego', 'CA', '92101', '6195555005');

INSERT INTO SUPPLIER VALUES
(1, 'Midwest Lumber Supply', 'Clark Kent', '4025556001', 30),
(2, 'Home Electrical Distributors', 'Diana Prince', '4025556002', 45),
(3, 'Precision Plumbing Supply', 'Bruce Wayne', '4025556003', 30),
(4, 'Quality Roofing Materials', 'Natasha Romanoff', '4025556004', 60),
(5, 'Interior Finish Warehouse', 'Steve Rogers', '4025556005', 30);

INSERT INTO PROJECT VALUES
(1, 1, '123 Maple Street', 'Omaha', 'NE', '68164', '2026-01-05', NULL, 'Active'),
(2, 2, '20 Ingram Street', 'Queens', 'NY', '11375', '2026-01-07', NULL, 'Active'),
(3, 3, '742 Evergreen Terrace', 'Springfield', 'IL', '62701', '2026-01-10', NULL, 'Active'),
(4, 4, '456 Oak Avenue', 'Seattle', 'WA', '98101', '2026-01-12', NULL, 'Active'),
(5, 5, '789 Pine Drive', 'San Diego', 'CA', '92101', '2026-01-15', NULL, 'Active');

INSERT INTO BID VALUES
(1, 1, '2026-01-06', 12, 75, 850, 1750, 'Approved'),   -- Bathroom remodel
(2, 2, '2026-01-08', 8, 70, 500, 1060, 'Approved'),    -- Roof patch
(3, 3, '2026-01-11', 10, 80, 650, 1450, 'Approved'),   -- Electrical upgrade
(4, 4, '2026-01-13', 6, 65, 400, 790, 'Approved'),     -- Plumbing repair
(5, 5, '2026-01-16', 14, 85, 900, 2090, 'Approved');   -- Kitchen cabinet install

INSERT INTO REPAIR VALUES
(1, 1, 'Replace bathroom vanity and plumbing fixtures', 12, 900),
(2, 2, 'Repair damaged roof shingles and seal flashing', 8, 560),
(3, 3, 'Upgrade electrical breaker panel to 200 amp', 10, 800),
(4, 4, 'Replace leaking kitchen sink drain line', 6, 390),
(5, 5, 'Install new kitchen cabinets and hardware', 14, 1190);

INSERT INTO MATERIAL VALUES
(1, 1, '2x4 Lumber', 'Standard framing lumber', 'Piece', 6.50),
(2, 2, '12 Gauge Electrical Wire', 'Copper residential wire', 'Foot', 1.25),
(3, 3, 'PVC Drain Pipe', '2 inch plumbing pipe', 'Foot', 3.75),
(4, 4, 'Architectural Roof Shingles', 'Weather resistant shingles', 'Bundle', 35.00),
(5, 5, 'Kitchen Cabinet Set', 'Preassembled cabinet units', 'Set', 750.00);

INSERT INTO REPAIR_MATERIAL VALUES
(1, 1, 15, 97.50),      -- Lumber used in vanity framing
(4, 2, 5, 175.00),      -- Shingles used
(2, 3, 120, 150.00),    -- Electrical wire
(3, 4, 20, 75.00),      -- PVC pipe
(5, 5, 1, 750.00);      -- Cabinet set

INSERT INTO SUPPLIER_PAYMENT VALUES
(1, 1, '2026-01-20', 500.00, 'Credit'),
(2, 2, '2026-01-21', 300.00, 'Wire'),
(3, 3, '2026-01-22', 250.00, 'Credit'),
(4, 4, '2026-01-23', 400.00, 'Card'),
(5, 5, '2026-01-24', 750.00, 'Wire');

INSERT INTO CUSTOMER_PAYMENT VALUES
(1, 1, 1, '2026-02-05', 1750.00, 'Card'),
(2, 2, 2, '2026-02-06', 1060.00, 'Card'),
(3, 3, 3, '2026-02-07', 1450.00, 'Wire'),
(4, 4, 4, '2026-02-08', 790.00, 'Cash'),
(5, 5, 5, '2026-02-09', 2090.00, 'Wire');
