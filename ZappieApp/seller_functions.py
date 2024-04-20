import random
from datetime import datetime
import mysql.connector as conn
import sys

admin = "nightfury"

def getProdID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Prod_ID FROM Product"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l)+1)

def sellerSignIn():
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()
    storeid = int(input("Enter Store ID: "))
    shopnum = input("Enter Shop No: ")
    cmd = "SELECT * FROM Store WHERE Store_ID = %s AND `Shop_No.` = %s"
    val = (storeid, shopnum)
    cursor.execute(cmd, val)
    result = cursor.fetchall()
    print(result)
    if (len(result) == 0):
        sellerid = -1
    else:
        sellerid = storeid
    print(sellerid)
    return sellerid

def addNewProduct(storeid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()

    # Gather product details from the user
    prod_id = getProdID()
    name = input("Enter Product Name: ")
    price = int(input("Enter Product Price: "))
    category = input("Enter Product Category: ")

    # Insert the new product into the Product table
    add_product_query = "INSERT INTO Product (Prod_ID, Name, Price, Category) VALUES (%s, %s, %s, %s)"
    product_data = (prod_id, name, price, category)

    cursor.execute(add_product_query, product_data)
    server.commit()

    print("Product added successfully.")

    # Insert the new product availability into the Availability table
    quantity = int(input("Enter Quantity: "))
    add_availability_query = "INSERT INTO Availability (Prod_ID, Store_ID, Quantity) VALUES (%s, %s, %s)"
    availability_data = (prod_id, storeid, quantity)

    cursor.execute(add_availability_query, availability_data)
    server.commit()

    print("Product availability added successfully.")

def increaseAvailability(storeid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()
    prod_id = int(input("Enter Product ID: "))
    addition = int(input("Enter Addition quantity: "))

    cmd = "UPDATE Availability SET Quantity = Quantity + %s WHERE Prod_ID = %s AND Store_ID = %s"
    val = (addition, prod_id, storeid)
    cursor.execute(cmd, val)
    server.commit()

def getInventorySummary(storeid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()
    cmd = "SELECT * FROM Availability WHERE Store_ID = %s"
    val = (storeid,)
    cursor.execute(cmd, val)
    
    # Fetch all rows from the result set
    rows = cursor.fetchall()

    print("Product ID\tQuantity")
    
    # Iterate over the rows and print each row
    for row in rows:
        print(f"{row[0]}\t\t{row[2]}")  # Assuming Prodct_ID is at index 0 and Quantity is at index 2

def getOrderHistory(storeid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()
    
    # SQL query to select order details from PickUp_Items table
    cmd = "SELECT * FROM PickUp_Items WHERE Store_ID = %s"
    val = (storeid,)
    cursor.execute(cmd, val)
    
    # Fetch all rows from the result set
    rows = cursor.fetchall()
    
    # Print the header
    print("Delivery Partner ID\tOrder ID\tStore ID\tDate and Time")
    
    # Iterate over the rows and print each row
    for row in rows:
        print(f"{row[0]}\t\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

def getOrderSummary(orderid):
    server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb")
    cursor = server.cursor()
    
    # SQL query to select order details from Order table
    cmd = "SELECT * FROM `Order` WHERE Order_ID = %s"
    val = (orderid,)
    cursor.execute(cmd, val)
    
    # Fetch the row from the result set
    row = cursor.fetchone()
    
    if row:
        # Print the header
        print("Order ID\tPlacing DateTime\tDelivery DateTime\tPayment Mode\tAmount\tStatus\tTransaction ID\tCustomer ID\tEmployee ID")
        
        # Print the order details
        print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")
        
        cartid = row[9]
        
        # SQL query to select product details added to the order
        cmd = "SELECT p.Prod_ID, p.Name, ap.Quantity FROM Product p JOIN added_products ap ON p.Prod_ID = ap.Prod_ID WHERE ap.Cart_ID = %s"
        val = (cartid,)
        cursor.execute(cmd, val)
        
        # Fetch all rows from the result set
        added_products = cursor.fetchall()
        
        # Print the added product details
        print("\nProducts Added:")
        print("Product ID\tName\tQuantity")
        for product in added_products:
            print(f"{product[0]}\t\t{product[1]}\t{product[2]}")
    else:
        print("Order not found.")

# getInventorySummary(3)
# increaseAvailability(3)
# addNewProduct(3)
# getOrderSummary(2012)