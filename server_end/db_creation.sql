-- create database and all required tables
CREATE SCHEMA IF NOT EXISTS Zappiedb;

CREATE TABLE `Zappiedb`.`Customer` (
  `Cust_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone_No` BIGINT NOT NULL,
  `Email` VARCHAR(120) NOT NULL,
  `House_No.` VARCHAR(45) NOT NULL,
  `Locality` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `PinCode` INT NOT NULL,
  PRIMARY KEY (`Cust_ID`));

CREATE TABLE `Zappiedb`.`Product` (
  `Prod_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Price` INT UNSIGNED NOT NULL,
  `Category` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Prod_ID`));

CREATE TABLE `Zappiedb`.`Store` (
  `Store_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Contact_No.` BIGINT NOT NULL,
  `Email` VARCHAR(100) NULL,
  `Shop_No.` VARCHAR(45) NOT NULL,
  `Locality` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `PinCode` INT NOT NULL,
  PRIMARY KEY (`Store_ID`));

CREATE TABLE `Zappiedb`.`DeliveryPartner` (
  `Emp_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone_No.` BIGINT NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Aadhar_No.` VARCHAR(12) NOT NULL,
  `PAN` VARCHAR(10) NOT NULL,
  `Salary` INT NOT NULL,
  `BankAccNo` VARCHAR(20) NOT NULL,
  `VehicleRegNo` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`Emp_ID`));

CREATE TABLE `Zappiedb`.`Order` (
  `Order_ID` INT NOT NULL,
  `PlacingDateTime` DATETIME NOT NULL,
  `DeliveryDateTime` DATETIME NOT NULL,
  `PaymentMode` VARCHAR(45) NOT NULL,
  `Amount` INT UNSIGNED NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `Trans_ID` VARCHAR(200) NOT NULL,
  `Cust_ID` INT NOT NULL,
  `Emp_ID` INT NOT NULL,
  PRIMARY KEY (`Order_ID`),
  INDEX `Cust_ID_idx` (`Cust_ID` ASC) VISIBLE,
  INDEX `Emp_ID_idx` (`Emp_ID` ASC) VISIBLE,
  CONSTRAINT `Cust_ID`
    FOREIGN KEY (`Cust_ID`)
    REFERENCES `Zappiedb`.`Customer` (`Cust_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Emp_ID`
    FOREIGN KEY (`Emp_ID`)
    REFERENCES `Zappiedb`.`DeliveryPartner` (`Emp_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Zappiedb`.`Order_Products` (
  `Order_ID` INT NOT NULL,
  `Product_ID` INT NOT NULL,
  PRIMARY KEY (`Order_ID`, `Product_ID`),
  INDEX `Product_ID_idx` (`Product_ID` ASC) VISIBLE,
  CONSTRAINT `Order_ID`
    FOREIGN KEY (`Order_ID`)
    REFERENCES `Zappiedb`.`Order` (`Order_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Product_ID`
    FOREIGN KEY (`Product_ID`)
    REFERENCES `Zappiedb`.`Product` (`Prod_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Zappiedb`.`PickUp_Items` (
  `DeliveryPartner_ID` INT NOT NULL,
  `Ord_ID` INT NOT NULL,
  `Store_ID` INT NOT NULL,
  `DateTime` DATETIME NOT NULL,
  PRIMARY KEY (`DeliveryPartner_ID`, `Ord_ID`, `Store_ID`),
  INDEX `Order_ID_idx` (`Ord_ID` ASC) VISIBLE,
  INDEX `Store_ID_idx` (`Store_ID` ASC) VISIBLE,
  CONSTRAINT `DeliveryPartner_ID`
    FOREIGN KEY (`DeliveryPartner_ID`)
    REFERENCES `Zappiedb`.`DeliveryPartner` (`Emp_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Ord_ID`
    FOREIGN KEY (`Ord_ID`)
    REFERENCES `Zappiedb`.`Order` (`Order_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Store_ID`
    FOREIGN KEY (`Store_ID`)
    REFERENCES `Zappiedb`.`Store` (`Store_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Zappiedb`.`Availability` (
  `Prodct_ID` INT NOT NULL,
  `Stor_ID` INT NOT NULL,
  `Quantity` INT UNSIGNED NULL,
  PRIMARY KEY (`Stor_ID`, `Prodct_ID`),
  INDEX `Product_ID_idx` (`Prodct_ID` ASC) VISIBLE,
  CONSTRAINT `Prodct_ID`
    FOREIGN KEY (`Prodct_ID`)
    REFERENCES `Zappiedb`.`Product` (`Prod_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Stor_ID`
    FOREIGN KEY (`Stor_ID`)
    REFERENCES `Zappiedb`.`Store` (`Store_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Zappiedb`.`Adds_Product` (
  `Prd_ID` INT NOT NULL,
  `Customer_ID` INT NOT NULL,
  `Quantity` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Customer_ID`, `Prd_ID`),
  INDEX `Prd_ID_idx` (`Prd_ID` ASC) VISIBLE,
  CONSTRAINT `Customer_ID`
    FOREIGN KEY (`Customer_ID`)
    REFERENCES `Zappiedb`.`Customer` (`Cust_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Prd_ID`
    FOREIGN KEY (`Prd_ID`)
    REFERENCES `Zappiedb`.`Product` (`Prod_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
   
