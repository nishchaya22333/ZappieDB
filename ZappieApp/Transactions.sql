-- CONFLICTING TRANSACTIONS

-- 1st Example
-- Consider the case where a particular store adds products to stock (i.e., increases the quantity), and simultaneously, a customer buys the same product (i.e. decreases the quantity)
-- Transaction 1: Store with Store_ID=1 increases the quantity of product with Prod_ID=3 by 3, A1 -> Availability table for Store_ID=1;

START TRANSACTION;
T1R1: SELECT Quantity INTO @current_Quantity FROM 'Availability' WHERE Store_ID=1 AND Prod_ID=3;
T1W1: UPDATE 'Product' SET Total_Quantity=@current_Quantity + 3 WHERE Prod_ID=3;
     UPDATE 'Availability' SET Quantity=@current_Quantity + 3 WHERE Store_ID=1 AND Prod_ID=3;
     COMMIT;

--Transaction 2: Customer with Cust_ID=1002 buys product with Prod_ID=3 and reduces the quantity by 4, AP2 -> added_product table for cart of Cust_ID = 1002

START TRANSACTION;
T2R2: SELECT Quantity INTO @current_Quantity FROM 'added_products' WHERE Prod_ID=3;
T2W2: UPDATE 'Product' SET Total_Quantity=@current_Quantity - 4 WHERE Prod_ID=3;
     UPDATE 'added_products' SET Quantity=4 WHERE Prod_ID=3 AND Cart_ID=SELECT Current_Cart FROM 'Customer' WHERE Cust_ID=1002;
     INSERT INTO cart (SELECT Current_Cart FROM 'Customer' WHERE Cust_ID=1002,1002,NOW());
     COMMIT;


-- 2nd Example
-- Two customers try to buy the same item at same time
-- Transaction 1: Customer with Cust_ID =  1001 wants to buy ‘2’ quantity of  product with Prod_ID = 13  (R(Qty), Qty = Qty - Q1, W(Qty), W(AP1))
-- Qty -> quantity of P1 as in table
-- AP1 -> added_product table for cart of Cust_ID = 1001
-- AP2 -> added_product table for cart of Cust_ID = 1002

START TRANSACTION;
SELECT Quantity INTO @current_quantity FROM 'Availability' WHERE Prod_ID = 13
UPDATE 'Availability' SET Quantity = @current_quantity - 2 WHERE Prod_ID = 13
INSERT INTO 'added_products' (Prod_ID, Quantity, Cart_ID) VALUES (13, 2, SELECT Current_Cart FROM 'Customer' WHERE Cust_ID = 1001)
COMMIT;

--Transaction 2 : Customer with Cust_ID =  1002 wants to buy ‘5’ quantity of  product with Prod_ID = 13  (R(Qty), Qty = Qty - Q2, W(Qty), W(AP2))

START TRANSACTION;
SELECT Quantity INTO @current_quantity FROM 'Availability' WHERE Prod_ID = 13
UPDATE 'Availability' SET Quantity = @current_quantity - 5 WHERE Prod_ID = 13
INSERT INTO 'added_products' (Prod_ID, Quantity, Cart_ID) VALUES (13, 2, SELECT Current_Cart FROM 'Customer' WHERE Cust_ID = 1002)
COMMIT;


-- NON COFLICTING TRANSACTIONS
-- Example 1:
-- T1 : Change the password of customer with customer ID = 1001
-- T2: Change the password of customer with customer ID = 1002


-- T1:
START TRANSACTION;
password1 = input("Enter new password: ")
UPDATE Customer SET Password = password1 WHERE Cust_ID = 1001;
COMMIT;

-- T2:
START TRANSACTION;
password2 = input("Enter new password: ")
UPDATE Customer SET Password = password2 WHERE Cust_ID = 1002;
COMMIT;

-- Example 2:
-- T1: Remove the product with product ID = 13 from added_products table of cart of customer with customer ID = 1001
-- T2: Remove the product with product ID = 14 from added_products table of cart of customer with customer ID = 1001

-- T1:
START TRANSACTION;
DELETE FROM added_products WHERE Prod_ID = 13  AND Cart_ID = (SELECT Current_Cart FROM customer where Cust_ID = 1001);
COMMIT;  

-- T2:
START TRANSACTION;
DELETE FROM added_products WHERE Prod_ID = 13  AND Cart_ID = (SELECT Current_Cart FROM customer where Cust_ID = 1001);
COMMIT; 


-- Example 3:
-- T1: Sign-In of customer with ID = 1001
-- T2: Sign-In of customer with ID = 1002

-- T1:
START TRANSACTION;
name1 = input("Enter e-mail : ")
pwd1 = input("Enter password : ")
SELECT * FROM Customer WHERE Email = name1 AND Password = pwd1
INSERT INTO cart (Cart_ID, Cust_ID, date_time) VALUES ((SELECT Current_Cart FROM customer where Cust_ID = 1001), 1001, NOW())
COMMIT;

-- T2:
START TRANSACTION;
name2 = input("Enter e-mail : ")
pwd2 = input("Enter password : ")
SELECT * FROM Customer WHERE Email = name2 AND Password = pwd2
INSERT INTO cart (Cart_ID, Cust_ID, date_time) VALUES ((SELECT Current_Cart FROM customer where Cust_ID = 1002), 1002, NOW())
COMMIT;


-- Example 4: 
-- T1: Store with Store_ID = 4,  updating the quantity of a product
-- T2: Store with Store_ID = 5,  updating the quantity of a product

-- T1:
START TRANSACTION;
prod_id1 = int(input("Enter Product ID: "))
addition1 = int(input("Enter Addition quantity: "))
UPDATE Availability SET Quantity = Quantity + addition1 WHERE Prod_ID = prod_id1 AND Store_ID = 4
COMMIT;


-- T2:
START TRANSACTION;
prod_id2 = int(input("Enter Product ID: "))
addition2 = int(input("Enter Addition quantity: "))
UPDATE Availability SET Quantity = Quantity + addition2 WHERE Prod_ID = prod_id2 AND Store_ID = 5
COMMIT;





