-- Modifying database to add a table cart to improve performance and ease of use.
CREATE TABLE `Zappiedb`.`Cart` (
  `Cart_ID` INT NOT NULL,
  `Custom_ID` INT NOT NULL,
  PRIMARY KEY (`Cart_ID`),
  INDEX `Cust_ID_idx` (`Custom_ID` ASC) VISIBLE,
  CONSTRAINT `Custom_ID`
    FOREIGN KEY (`Custom_ID`)
    REFERENCES `Zappiedb`.`Customer` (`Cust_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

USE Zappiedb;

DROP TABLE `Order_Products`;

-- Former adds_product table is modified to added_products in accordance with the updated database design.
ALTER TABLE `adds_product` DROP Constraint `Customer_ID`;
ALTER TABLE `adds_product` DROP COLUMN `Customer_ID`;
ALTER TABLE  `adds_product` ADD COLUMN `Cart_ID` INT;
ALTER TABLE `adds_product` RENAME `added_products`;

ALTER TABLE `added_products` ADD FOREIGN KEY (`Cart_ID`) REFERENCES `Cart`(`Cart_ID`);

ALTER TABLE `Customer` 
ADD COLUMN `Current_Cart` INT NULL AFTER `PinCode`;

ALTER TABLE `Customer` 
ADD CONSTRAINT `Current_Cart`
  FOREIGN KEY (`Current_Cart`)
  REFERENCES `Zappiedb`.`Cart` (`Cart_ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `Order`
ADD COLUMN `Cart_ID` INT NOT NULL,
ADD CONSTRAINT `fk_Cart_ID`
FOREIGN KEY (`Cart_ID`)
REFERENCES `Zappiedb`.`Cart`(`Cart_ID`);

-- ALTER TABLE `added_products` DROP Constraint `Prd_ID`;
ALTER TABLE `added_products` DROP PRIMARY KEY;

-- Renaming columns to ensure uniform naming convention to facilitate smooth query calls from server-end programs.
ALTER TABLE Cart
RENAME COLUMN Custom_ID TO Cust_ID;

ALTER TABLE `Availability`
RENAME COLUMN `Prodct_ID` TO `Prod_ID`; 

ALTER TABLE `Availability`
RENAME COLUMN `Stor_ID` TO `Store_ID`;

ALTER TABLE `added_products` 
RENAME COLUMN `Prd_ID` TO `Prod_ID`;

ALTER TABLE `customer` 
ADD COLUMN `Password` varchar(400) NOT NULL;

ALTER TABLE `cart` 
ADD COLUMN `date_time` DATETIME NOT NULL;

ALTER TABLE `cart` 
ADD COLUMN `date_time` DATETIME NOT NULL;


ALTER TABLE `DeliveryPartner`
ADD COLUMN `rating` FLOAT;

ALTER TABLE `DeliveryPartner`
ADD COLUMN `status` VARCHAR(40);

ALTER TABLE `Order` 
ADD COLUMN `Feedback` VARCHAR(200);

