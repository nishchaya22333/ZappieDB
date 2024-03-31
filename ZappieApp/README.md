This folder contains all necessary files to run a basic version of Zapppie. 
- `db_creation.sql` and `db_modifications` have all necessary SQL queries to initialize the database.
- `data_insertion.sql` has queries to input mock data for testing.

## Initialize the database:
### a. Using App.py
1. Run App.py
2. Access admin portal
3. Choose correct option and proceed.
4. You will see a Server login page, enter credentials.

### b. Using GUI_boot.py
1. Run GUI_boot.py
2. You will see a Server login page, enter credentials.

### c. Using CLI_boot.py
1. Run CLI_boot.py
2. You will be prompted to enter required credentials on terminal.

**Caution:** Please make sure there is no duplicate database/schema on the server with the name Zappiedb before initializing the database.

**Note:** In case, errors are encountered, try using absolute paths for accessing SQL query files instead of relative path which is currently being used. (Relative path is preferred to ensure smooth functioning across different systems)

**Note:** Please make sure you are using correct credentials in customer_analysis.py while connecting to MySQL server.

Further to use currently working services, access the customer portal using App.py

--------------------------------------------------------------------------------------

## Contribution
- **2022025 Aditi Sharma:** Customer Services' Functions, Testing/Debugging, Mock Data Insertion
- **2022068 Ananya Garg:** SQL queries, Debugging, Database Creation
- **2022276 Manas Chhabra:** Customer Services' Functions, Basic Interface
- **2022333 Nishchaya Roy:** Database Initialization, Customer Services' Functions, Basic Interface
