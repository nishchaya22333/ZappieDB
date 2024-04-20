import random
from datetime import datetime
import mysql.connector as conn
import sys

admin = "nightfury"

def empSignIn():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()

    empid = int(input("Enter Employee ID: "))
    emppass = int(input("Enter Password: "))
    cmd = "SELECT * FROM DeliveryPartner WHERE Emp_ID = %s AND `PAN` = %s"
    val = (empid, emppass)
    cursor.execute(cmd, val)
    result = cursor.fetchall()
    print(result)
    if (len(result) == 0):
        id = -1
    else:
        id = empid
    print(id)
    return id

def get_personal_details(empid):
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    sql = "SELECT * FROM DeliveryPartner WHERE Emp_id = %s"
    cursor.execute(sql, (empid,))
    result = cursor.fetchone()
    if result:
                print("Personal Details:")
                print("Employee ID:", result[0])
                print("Name:", result[1])
                print("Email:", result[2])
                print("Phone:", result[3])
    else:
                print("Employee not found.")

def view_delivery_history(empid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()

    # Define the SQL query with placeholders
    cmd = "SELECT o.Order_ID, o.PlacingDateTime, o.DeliveryDateTime, o.PaymentMode, o.Amount, o.Status, o.Trans_ID, o.Cust_ID, o.Emp_ID FROM `Order` AS o INNER JOIN DeliveryPartner AS d ON o.Emp_ID = d.Emp_ID WHERE o.Emp_ID = %s"

    # Execute the query with the provided parameter
    cursor.execute(cmd, (empid,))

    # Fetch the results
    result = cursor.fetchall()
    if result:
        for row in result:
            print("Order ID:", row[0])
            print("Placing Date and Time:", row[1])
            print("Delivery Date and Time:", row[2])
            print("Payment Mode:", row[3])
            print("Amount:", row[4])
            print("Status:", row[5])
            print("Transaction ID:", row[6])
            print("Customer ID:", row[7])
            print("Employee ID:", row[8])
    else:
        print("No delivery history found")

# get_personal_details(2)
view_delivery_history(2)
