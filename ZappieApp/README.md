# Zappie Basic Version

This folder contains all necessary files to run a basic version of Zappie.

## Files:
- `db_creation.sql`: Contains SQL queries to initialize the database.
- `db_modifications.sql`: Contains SQL queries for database modifications.
- `data_insertion.sql`: Contains SQL queries to input mock data for testing.

## Initialize the Database:

### a. Using App.py
1. Run App.py.
2. Access the admin portal.
3. Choose the correct option and proceed.
4. You will see a Server login page, enter credentials.

### b. Using GUI_boot.py
1. Run GUI_boot.py.
2. You will see a Server login page, enter credentials.

### c. Using CLI_boot.py
1. Run CLI_boot.py.
2. You will be prompted to enter required credentials on the terminal.

**Caution:** Please make sure there is no duplicate database/schema on the server with the name Zappiedb before initializing the database.

**Note:** In case errors are encountered, try using absolute paths for accessing SQL query files instead of relative paths, which are currently being used. (Relative path is preferred to ensure smooth functioning across different systems)

**Note:** Please make sure you are using correct credentials in `customer_analysis.py` while connecting to the MySQL server.

## Usage:
To use the currently working services, access the customer portal using `App.py`.

# User Guide for Application

## Introduction:
The application provides access to various functions tailored for administrators, sellers, customers, and employees.

## Features Overview:
- **Boot Server and Database Creation**
- **Administrator Access**
  - Add Store
  - Add Employee
  - Get Store Analysis
  - Get Employee Analysis
- **Seller Access**
  - Add New Product
  - Increase Availability
  - Get Inventory Summary
  - Get Order History
  - Get Order Summary
- **Customer Access**
  - Sign In
  - Sign Up
  - Show All Products
  - Search Product
  - Add Product
  - Remove Product
  - Place Order
  - My Analysis
- **Employee Access**
  - Get Personal Details
  - Edit Profile
  - View Delivery History
  - View Rating

## Getting Started:
To begin using the application, follow these steps:

### A. Boot Server and Create Database
Select the option to boot the server and create the database if the server is in its initial state. This step ensures proper initialization of the system.

### B. Log In
Choose the appropriate user role:
- Admin Login
- Seller Login
- Employee Login
Enter your credentials to proceed.

## Detailed Functionality:

### Administrator Access:
1. **Add Store**
   - Add a new store to the system.
2. **Add Employee**
   - Register a new employee within the system.
3. **Get Store Analysis**
   - Obtain an analysis report for a specific store.
4. **Get Employee Analysis**
   - Retrieve an analysis report for employees.

### Seller Access:
1. **Add New Product**
   - Add a new product to the inventory of a store.
2. **Increase Availability**
   - Increase the availability of an existing product.
3. **Get Inventory Summary**
   - View a summary of the inventory for a specific store.
4. **Get Order History**
   - Access the order history for a store.
5. **Get Order Summary**
   - View a summary of a specific order.

### Customer Access:
1. **Sign In**
   - Log in as a customer to access account features.
2. **Sign Up**
   - Register as a new customer.
3. **Show All Products**
   - Display all available products.
4. **Search Products**
   - Search for specific products.
5. **Add Product**
   - Add a product to the customer's shopping list.
6. **Remove Product**
   - Remove a product from the customer's shopping list.
7. **Place Order**
   - Finalize the shopping list and place an order.
8. **My Analysis**
   - Access personalized analysis and recommendations.

### Employee Access:
1. **Get Personal Details**
   - Retrieve personal details associated with the employee account.
2. **Edit Profile**
   - Update personal profile information.
3. **View Delivery History**
   - Access the delivery history associated with the employee account.
4. **View Rating**
   - View the rating assigned to the employee.

## Logging Out:
- To log out from the application, simply choose the "Log Out" option from the menu.
- The system will prompt confirmation before logging out to ensure user action
