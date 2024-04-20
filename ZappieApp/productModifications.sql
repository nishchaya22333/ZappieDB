ALTER TABLE Product
ADD COLUMN Total_Quantity INT UNSIGNED;

UPDATE Product AS p
JOIN (
    SELECT Prod_ID, SUM(Quantity) AS Total_Quantity
    FROM Availability
    GROUP BY Prod_ID
) AS a ON p.Prod_ID = a.Prod_ID
SET p.Total_Quantity = a.Total_Quantity; 