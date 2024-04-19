import art
import GUI_boot
import getpass
import admin_funtions

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
        pass
        #1 add new product 2. increase availibility 3. get inventory summary 4. get order summary
    elif (choice == "4"):
        pass
        # 1. get personal details 2. edit personal details 3. view delivery history 4. view rating
    else:
        print(art.dog)
        print("Invalid Choice.")
# main()
