INSERT INTO `Zappiedb`.`Store` (`Store_ID`,`Name`, `Contact_No.`, `Email`, `Shop_No.`, `Locality`, `City`, `PinCode`) VALUES
(1, 'Max Super Store', 12345678900, 'maxstore@example.com', 'Shop 1, ABC Market', 'Rohini', 'New Delhi', 110085),
(2, 'Sasta Bazar', 98765432101, 'sastabazar@example.com', 'Shop 2, Main Road', 'Karol Bagh', 'New Delhi', 110005),
(3, 'Reliance Fresh', 01234567892, 'reliancefresh@example.com', 'Shop 3, Mall Road', 'Ghaziabad', 'Uttar Pradesh', 201001),
(4, 'Big Bazaar', 99887766553, 'bigbazaar@example.com', 'Shop 4, MG Road', 'Gurgaon', 'Haryana', 122001),
(5, 'Fresh & Go', 88888888884, 'freshngo@example.com', 'Shop 5, Market Square', 'Noida', 'Uttar Pradesh', 201301),
(6, 'Happy Mart', 77777777775, 'happymart@example.com', 'Shop 6, Station Road', 'Faridabad', 'Haryana', 121001),
(7, 'Apna Bazaar', 66666666666, 'apnabazaar@example.com', 'Shop 7, Nehru Nagar', 'Jaipur', 'Rajasthan', 302001),
(8, 'Spar', 55555555557, 'spar@example.com', 'Shop 8, High Street', 'Pune', 'Maharashtra', 411001),
(9, 'Super Value', 44444444448, 'supervalue@example.com', 'Shop 9, Gandhi Road', 'Bangalore', 'Karnataka', 560001),
(10, 'More', 33333333339, 'more@example.com', 'Shop 10, Anna Nagar', 'Chennai', 'Tamil Nadu', 600001);

INSERT INTO Zappiedb.Product (Prod_ID, Name, Price, Category) VALUES 
(1, 'Organic Brown Rice (1kg)', 149, 'Food'),
(2, 'Organic Chicken Eggs (Dozen)', 69, 'Food'),
(3, 'Organic Tomatoes (500g)', 39, 'Fruits & Vegetables'),
(4, 'Organic Bananas (Pack of 6)', 29, 'Fruits & Vegetables'),
(5, 'Organic Spinach (250g)', 25, 'Fruits & Vegetables'),
(6, 'Organic Honey (500g)', 199, 'Food'),
(7, 'Organic Whole Milk (1 liter)', 79, 'Food'),
(8, 'Handmade Shea Butter Soap (Pack of 3)', 99, 'Daily Care'),
(9, 'Natural Coconut Oil (250ml)', 149, 'Daily Care'),
(10, 'Organic Green Tea (50g)', 149, 'Food'),
(11, 'Organic Brown Sugar (1kg)', 99, 'Food'),
(13, 'Organic Oranges (Pack of 4)', 49, 'Fruits & Vegetables'),
(14, 'Organic Apples (Pack of 6)', 59, 'Fruits & Vegetables'),
(12, 'Organic Milk (1L)', 79, 'Food'),
(16, 'Organic Carrots (500g)', 35, 'Fruits & Vegetables'),
(17, 'Organic Potatoes (1kg)', 45, 'Fruits & Vegetables'),
(18, 'Organic Broccoli (500g)', 55, 'Fruits & Vegetables'),
(23, 'Organic Cucumbers (Pack of 3)', 39, 'Fruits & Vegetables'),
(22, 'Organic Bell Peppers (Pack of 4)', 69, 'Fruits & Vegetables'),
(21, 'Organic Lettuce (250g)', 29, 'Fruits & Vegetables'),
(34, 'Organic Strawberries (250g)', 79, 'Fruits & Vegetables'),
(45, 'Organic Blueberries (250g)', 89, 'Fruits & Vegetables'); 

INSERT INTO Zappiedb.DeliveryPartner (Emp_ID, Name, `Phone_No.`, Email, `Aadhar_No.`, PAN, Salary, BankAccNo, VehicleRegNo) VALUES
(1, 'John Smith', 9876543210, 'john.smith@example.com', '123456789012', 'ABCDE1234F', 30000, '1234567890123456', 'MH123456'),
(2, 'Emma Johnson', 9876543211, 'emma.johnson@example.com', '234567890123', 'BCDEF2345G', 32000, '2345678901234567', 'KA234567'),
(3, 'Michael Williams', 9876543212, 'michael.williams@example.com', '345678901234', 'CDEFG3456H', 35000, '3456789012345678', 'TN345678'),
(4, 'Sophia Brown', 9876543213, 'sophia.brown@example.com', '456789012345', 'DEFGH4567I', 33000, '4567890123456789', 'UP456789'),
(5, 'Daniel Martinez', 9876543214, 'daniel.martinez@example.com', '567890123456', 'EFGHI5678J', 34000, '5678901234567890', 'MH567890'),
(6, 'Olivia Garcia', 9876543215, 'olivia.garcia@example.com', '678901234567', 'FGHIJ6789K', 31000, '6789012345678901', 'DL678901'),
(7, 'David Rodriguez', 9876543216, 'david.rodriguez@example.com', '789012345678', 'GHIJK7890L', 36000, '7890123456789012', 'GJ789012'),
(8, 'Isabella Lopez', 9876543217, 'isabella.lopez@example.com', '890123456789', 'HIJKL8901M', 37000, '8901234567890123', 'KL890123'),
(9, 'Alexander Lee', 9876543218, 'alexander.lee@example.com', '901234567890', 'IJKLM9012N', 38000, '9012345678901234', 'HR901234'),
(10, 'Sophia Scott', 9876543219, 'sophia.scott@example.com', '012345678901', 'JKLMN0123O', 33000, '0123456789012345', 'BR012345');

INSERT INTO `Zappiedb`.`Order` (`Order_ID`, `PlacingDateTime`, `DeliveryDateTime`, `Amount`, `Status`, `Trans_ID`, `Cust_ID`, `Emp_ID`, `Cart_ID`)
VALUES 
(2000, '2024-03-30 10:00:00', '2024-04-02 14:00:00', 150, 'Delivered', 'T123', 1001, 1, 1),
(2001, '2024-03-30 11:00:00', '2024-04-02 15:00:00', 200, 'Delivered', 'T124', 1001, 2, 2),
(2002, '2024-03-30 12:00:00', '2024-04-02 16:00:00', 250, 'Pending', 'T125', 1002, 3, 3),
(2003, '2024-03-30 13:00:00', '2024-04-02 17:00:00', 300, 'Delivered', 'T126', 1002, 4, 4),
(2004, '2024-03-30 14:00:00', '2024-04-02 18:00:00', 350, 'Delivered', 'T127', 1003, 5, 5),
(2005, '2024-03-30 15:00:00', '2024-04-02 19:00:00', 400, 'Pending', 'T128', 1003, 6, 6),
(2006, '2024-03-30 16:00:00', '2024-04-02 20:00:00', 450, 'Pending', 'T129', 1004, 7, 7),
(2007, '2024-03-30 17:00:00', '2024-04-02 21:00:00', 500, 'Delivered', 'T130', 1004, 8, 8),
(2008, '2024-03-30 18:00:00', '2024-04-02 22:00:00', 550, 'Delivered', 'T131', 1005, 9, 9),
(2009, '2024-03-30 19:00:00', '2024-04-02 23:00:00', 600, 'Pending', 'T132', 1005, 10, 10),
(2010, '2024-03-30 20:00:00', '2024-04-03 00:00:00', 650, 'Delivered', 'T133', 1006, 1, 11),
(2011, '2024-03-30 21:00:00', '2024-04-03 01:00:00', 700, 'Pending', 'T134', 1006, 2, 12),
(2012, '2024-03-30 22:00:00', '2024-04-03 02:00:00', 750, 'Pending', 'T135', 1007, 3, 13),
(2013, '2024-03-30 23:00:00', '2024-04-03 03:00:00', 800, 'Delivered', 'T136', 1007, 4, 14),
(2014, '2024-03-31 00:00:00', '2024-04-03 04:00:00', 850, 'Pending', 'T137', 1008, 5, 15),
(2015, '2024-03-31 01:00:00', '2024-04-03 05:00:00', 900, 'Delivered', 'T138', 1008, 6, 16),
(2016, '2024-03-31 02:00:00', '2024-04-03 06:00:00', 950, 'Pending', 'T139', 1009, 7, 17),
(2017, '2024-03-31 03:00:00', '2024-04-03 07:00:00', 1000, 'Delivered', 'T140', 1009, 8, 18),
(2018, '2024-03-31 04:00:00', '2024-04-03 08:00:00', 1050, 'Delivered', 'T141', 1010, 9, 19),
(2019, '2024-03-31 05:00:00', '2024-04-03 09:00:00', 1100, 'Pending', 'T142', 1010, 10, 20),
(2020, '2024-03-31 06:00:00', '2024-04-03 10:00:00', 1150, 'Delivered', 'T143', 1011, 1, 21),
(2021, '2024-03-31 07:00:00', '2024-04-03 11:00:00', 1200, 'Pending', 'T144', 1011, 2, 22),
(2022, '2024-03-31 08:00:00', '2024-04-03 12:00:00', 1250, 'Delivered', 'T145', 1012, 3, 23),
(2023, '2024-03-31 09:00:00', '2024-04-03 13:00:00', 1300, 'Pending', 'T146', 1012, 4, 24);




INSERT INTO `cart` (`Cart_ID`, `Cust_ID`, `date_time`)
VALUES 
(1, 1001, '2024-03-01 08:00:00'), (2, 1001, '2024-03-02 09:00:00'), 
(3, 1002, '2024-03-03 10:00:00'), (4, 1002, '2024-03-04 11:00:00'), 
(5, 1003, '2024-03-05 12:00:00'), (6, 1003, '2024-03-06 13:00:00'), 
(7, 1004, '2024-03-07 14:00:00'), (8, 1004, '2024-03-08 15:00:00'), 
(9, 1005, '2024-03-09 16:00:00'), (10, 1005, '2024-03-10 17:00:00'),
(11, 1006, '2024-02-01 18:00:00'), (12, 1006, '2024-02-02 19:00:00'), 
(13, 1007, '2024-02-03 20:00:00'), (14, 1007, '2024-02-04 21:00:00'), 
(15, 1008, '2024-02-05 22:00:00'), (16, 1008, '2024-01-01 23:00:00'),
(18, 1009, '2024-01-03 01:00:00'), (19, 1010, '2024-01-04 02:00:00'), 
(20, 1010, '2024-01-05 03:00:00'), (17, 1009, '2024-01-02 00:00:00'), 
(21, 1011, '2023-12-01 04:00:00'), (22, 1011, '2023-12-02 05:00:00'), 
(23, 1012, '2023-12-03 06:00:00'), (24, 1012, '2023-12-04 07:00:00');


INSERT INTO `added_products` (`Cart_ID`, `Prd_ID`, `Quantity`)
VALUES (1, 11, 3), (2, 13, 2), (3, 14, 4), (4, 11, 4), (5, 12, 4),
(6, 13, 2), (7, 11, 2), (8, 16, 3), (9, 17, 2), (10, 18, 2),
(11, 11, 2), (11, 23, 2), (12, 22, 5), (12, 2, 3), (13, 3, 3),
(13, 22, 4), (14, 21, 5), (14, 34, 2), (15, 23, 2), (15, 45, 4),
(16, 9, 3), (16, 34, 3), (17, 23, 4), (17, 12, 4), (18, 6, 4),
(18, 34, 5), (19, 3, 4), (19, 34, 4), (20, 1, 3), (20, 5, 5),
(21, 4, 5), (21, 3, 4), (22, 34, 2), (22, 23, 5), (23, 3, 4),
(23, 22, 4), (24, 12, 4), (24, 10, 2);

