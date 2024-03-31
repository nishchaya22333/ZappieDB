-- Trigger creation 

CREATE TRIGGER update_availability_on_product_removal
AFTER DELETE ON added_products
FOR EACH ROW
BEGIN
    DECLARE prod_quantity INT;
    SELECT Quantity INTO prod_quantity FROM Availability WHERE Prod_ID = OLD.Prod_ID;
    UPDATE Availability SET Quantity = prod_quantity + OLD.Quantity WHERE Prod_ID = OLD.Prod_ID;
END;

CREATE TRIGGER update_availability_after_add
AFTER INSERT ON added_products
FOR EACH ROW
BEGIN
    DECLARE available_quantity INT;
    SELECT Quantity INTO available_quantity FROM Availability WHERE Prod_ID = NEW.Prod_ID;
    UPDATE Availability SET Quantity = available_quantity - NEW.Quantity WHERE Prod_ID = NEW.Prod_ID;
END;

CREATE TRIGGER set_delivery_date_time
BEFORE INSERT ON `Order`
FOR EACH ROW
BEGIN
    SET NEW.DeliveryDateTime = NULL;
END;