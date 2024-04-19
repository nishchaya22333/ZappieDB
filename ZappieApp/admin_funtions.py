import random
from datetime import datetime
import mysql.connector as conn
import sys

admin = "password"

def getStoreid():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Store_ID FROM Store"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l)+1)

def getEmpid():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Emp_ID FROM DeliveryPartner"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l)+1)

def registerStore():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    storeid = getStoreid()
    name = input("Enter Name: ")
    contact_no = int(input("Enter Contact No.: "))
    email = input("Enter Email: ")
    shop_no = input("Enter Shop No.: ")
    locality = input("Enter Locality: ")
    city = input("Enter City: ")
    pincode = int(input("Enter PinCode: "))
    
    cmd  = "INSERT INTO Store (Store_ID, Name, Contact_No., Email, Shop_No., Locality, City, PinCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (storeid, name, contact_no, email, shop_no, locality, city, pincode)

    cursor.execute(cmd, val)
    server.commit()
    print("Store registered successfully!")
    

def registerEmployee():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    empid = getEmpid()
    empid = getEmpid()
    name = input("Enter Name: ")
    phone_no = int(input("Enter Phone No.: "))
    email = input("Enter Email: ")
    aadhar_no = input("Enter Aadhar No.: ")
    pan = input("Enter PAN: ")
    salary = int(input("Enter Salary: "))
    bank_acc_no = input("Enter Bank Account No.: ")
    vehicle_reg_no = input("Enter Vehicle Registration No.: ")

    cmd = "INSERT INTO DeliveryPartner (Emp_ID, Name, Phone_No., Email, Aadhar_No., PAN, Salary, BankAccNo, VehicleRegNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (empid, name, phone_no, email, aadhar_no, pan, salary, bank_acc_no, vehicle_reg_no)

    cursor.execute(cmd, val)
    server.commit()
    print("Employee registered successfully!")


def getStoreAnalysis():
    server = conn.connect(host="localhost", user="root", password="admin", database="zappiedb")
    cursor = server.cursor()

    # Get total number of stores
    cursor.execute("SELECT COUNT(*) FROM Store")
    total_stores = cursor.fetchone()[0]

    # Get number of stores with email addresses
    cursor.execute("SELECT COUNT(*) FROM Store WHERE Email IS NOT NULL")
    stores_with_email = cursor.fetchone()[0]

    # Get the most common city
    cursor.execute("SELECT City, COUNT(*) AS count FROM Store GROUP BY City ORDER BY count DESC LIMIT 1")
    most_common_city = cursor.fetchone()

    # Print the analysis/summary
    print("Store Table Analysis:")
    print("====================")
    print(f"Total number of stores: {total_stores}")
    print(f"Number of stores with email addresses: {stores_with_email}")
    if most_common_city:
        print(f"Most common city: {most_common_city[0]} ({most_common_city[1]} stores)")
    else:
        print("No data available for most common city.")
    # Query to get the number of stores in each locality
    sql = "SELECT Locality, COUNT(*) AS StoreCount FROM Store GROUP BY Locality"
    cursor.execute(sql)
    store_counts = cursor.fetchall()
    print("Number of stores in each locality:")
    print("==================================")
    for locality, count in store_counts:
        print(f"{locality}: {count}")



def getEmployeeAnalysis():
    server = conn.connect(host="localhost", user="root", password="admin", database="zappiedb")
    cursor = server.cursor()

    # Get total count of employees
    cursor.execute("SELECT COUNT(*) FROM DeliveryPartner")
    total_employees = cursor.fetchone()[0]

    # Analysis based on salary
    cursor.execute("SELECT MIN(Salary), MAX(Salary), AVG(Salary) FROM DeliveryPartner")
    min_salary, max_salary, avg_salary = cursor.fetchone()

    # Print the analysis
    print("Employee Analysis:")
    print("==================")
    print(f"Total number of employees: {total_employees}")
    print(f"Minimum salary: {min_salary}")
    print(f"Maximum salary: {max_salary}")
    print(f"Average salary: {avg_salary:.2f}")
