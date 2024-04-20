import art
import GUI_boot
import getpass
import admin_funtions
import seller_functions
import emp_functions

def admin_access():
    # print("ok")
    choice = input("1. Add store \n2. Add Employee \n3. Get Store Analysis \n4. Get Employee Analysis \nEnter your choice: ")
    if (choice == "1"):
        admin_funtions.registerStore()
    elif (choice == "2"):
        admin_funtions.registerEmployee()
    elif (choice == "3"):
        admin_funtions.getStoreAnalysis()
    elif (choice == "4"):
        admin_funtions.getEmployeeAnalysis()
    else:
        print(art.traffic)
        print("Invalid Choice.")

def seller_access():
    storeid = seller_functions.sellerSignIn()
    if (storeid == -1):
        print("Sign In Failed")
    else:
        print("Sign in successful")
        while(True):
            choice = input("1. Add New Product \n2. Increase Availibility \n3. Get Inventory Summary \n4. Get Order History \n5. Get Order Summary \n5. Log Out \nEnter your choice: ")
            if (choice == "1"):
                seller_functions.addNewProduct(storeid)
            elif (choice == "2"):
                seller_functions.increaseAvailability(storeid)
            elif (choice == "3"):
                seller_functions.getInventorySummary(storeid)
            elif (choice == "4"):
                seller_functions.getOrderHistory(storeid)
            elif (choice == "5"):
                orderid = int(input("Enter Order ID to get summary: "))
                seller_functions.getOrderSummary(orderid)
            elif (choice == "6"):
                print("Store ID:", storeid, "Logged Out")
                storeid = -1
                break
            else:
                print(art.traffic)
                print("Invalid Choice.")
    
def emp_access():
    empid = emp_functions.empSignIn()
    if (empid == -1):
        print("Sign In Failed")
    else:
        while(True):
            choice = input("1. Get Personal Details \n2. Edit Profile \n3. View Delivery History \n4. View Rating \n5. Log Out \nEnter your choice: ")
            if (choice == "1"):
                emp_functions.get_personal_details(empid)
            elif (choice == "2"):
                pass
            elif (choice == "3"):
                pass
            elif (choice == "4"):
                pass
            elif (choice == "5"):
                print("Employee ID:", empid, "Logged Out")
                storeid = -1
                break
            else:
                print(art.traffic)
                print("Invalid Choice.")


def main():
    choice = input("1. Boot server and create database \n2. Admin LogIn \n3. Seller LogIn \n4. Employee LogIn \nEnter your choice: ")
    if (choice == "1"):
        warning_message = "Proceed only if server is in initial state. Attempt to duplicate database will lead to termination."
        print("\u26A0"+"\033[91mWarning: \033[0m" + " " + warning_message)
        proceed = int(input("1. Continue\n2. Cancel\nEnter your choice: "))
        if proceed == 1:
            GUI_boot.main()
    elif (choice == "2"):
        x = input("Enter username: ")
        y = getpass.getpass("Enter password: ")
        if(x == "admin" and y == "admin"):
            admin_access()
    elif (choice == "3"):
        seller_access()
        #1 add new product 2. increase availibility 3. get inventory summary 4. get order summary

    elif (choice == "4"):
        emp_access()
        # 1. get personal details 2. edit personal details 3. view delivery history 4. view rating
    else:
        print(art.dog)
        print("Invalid Choice.")
# main()
