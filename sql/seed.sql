INSERT INTO users (first_name, last_name, email, phone, address_line1, city, state, pincode)
VALUES
('Amit', 'Sharma', 'amit.sharma@example.com', '9876543210', '12 MG Road', 'Bangalore', 'Karnataka', '560001'),
('Priya', 'Patel', 'priya.patel@example.com', '9812345678', '45 Nehru Street', 'Mumbai', 'Maharashtra', '400001'),
('Rahul', 'Verma', 'rahul.verma@example.com', '9871234567', '78 Anna Nagar', 'Chennai', 'Tamil Nadu', '600040'),
('Sneha', 'Nair', 'sneha.nair@example.com', '9845123456', '34 Marine Drive', 'Kochi', 'Kerala', '682001'),
('Vikram', 'Singh', 'vikram.singh@example.com', '9887766554', '89 Sector 22', 'Chandigarh', 'Chandigarh', '160022'),
('Neha', 'Gupta', 'neha.gupta@example.com', '9822334455', '56 Park Street', 'Kolkata', 'West Bengal', '700016'),
('Arjun', 'Reddy', 'arjun.reddy@example.com', '9966554433', '23 Jubilee Hills', 'Hyderabad', 'Telangana', '500033'),
('Divya', 'Menon', 'divya.menon@example.com', '9811998877', '90 Race Course Road', 'Coimbatore', 'Tamil Nadu', '641018'),
('Ravi', 'Kumar', 'ravi.kumar@example.com', '9797979797', '67 Patel Nagar', 'Delhi', 'Delhi', '110008'),
('Ananya', 'Das', 'ananya.das@example.com', '9898989898', '11 Park Avenue', 'Bhubaneswar', 'Odisha', '751001');

INSERT INTO employment_info (user_id, company_name, designation, start_date, end_date, is_current)
VALUES
(1, 'Infosys', 'Software Engineer', '2021-06-01', NULL, TRUE),
(2, 'TCS', 'Data Analyst', '2020-01-15', '2022-12-31', FALSE),
(3, 'Wipro', 'Developer', '2022-03-10', NULL, TRUE),
(4, 'Accenture', 'HR Executive', '2019-07-01', '2023-01-15', FALSE),
(5, 'Tech Mahindra', 'System Admin', '2020-09-01', NULL, TRUE),
(6, 'Cognizant', 'QA Engineer', '2021-04-20', NULL, TRUE),
(7, 'Amazon', 'Cloud Engineer', '2018-11-05', '2023-09-30', FALSE),
(8, 'Flipkart', 'Data Engineer', '2023-02-01', NULL, TRUE),
(9, 'Google', 'Project Manager', '2020-05-15', NULL, TRUE),
(10, 'IBM', 'Business Analyst', '2019-09-09', '2022-09-09', FALSE);


INSERT INTO user_bank_info (user_id, bank_name, account_number, ifsc, account_type)
VALUES
(1, 'HDFC Bank', '1234567890', 'HDFC0001234', 'Savings'),
(2, 'ICICI Bank', '2345678901', 'ICIC0002345', 'Current'),
(3, 'State Bank of India', '3456789012', 'SBIN0003456', 'Savings'),
(4, 'Axis Bank', '4567890123', 'UTIB0004567', 'Current'),
(5, 'Kotak Mahindra Bank', '5678901234', 'KKBK0005678', 'Savings'),
(6, 'Canara Bank', '6789012345', 'CNRB0006789', 'Savings'),
(7, 'Punjab National Bank', '7890123456', 'PUNB0007890', 'Current'),
(8, 'Federal Bank', '8901234567', 'FDRL0008901', 'Savings'),
(9, 'IndusInd Bank', '9012345678', 'INDB0009012', 'Savings'),
(10, 'Union Bank of India', '1122334455', 'UBIN0001122', 'Current');


