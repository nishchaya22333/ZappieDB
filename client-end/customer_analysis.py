import random
from datetime import datetime
import mysql.connector as conn
import sys
# Global
custID = -1

admin = "password"

def getCartID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Cart_ID FROM cart"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)

def getCustID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Cust_ID FROM customer"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)

def getOrdertID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Order_ID FROM Order"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)

def signUp():
    server = conn.connect(host="localhost", user="root", password = admin, database="zappiedb", autocommit=True)
    cursor = server.cursor()

    # Input customer data
    cust_id = getCustID()
    name = input("Enter name: ")
    phone_no = int(input("Enter phone number: "))
    email = input("Enter email: ")
    house_no = input("Enter house number: ")
    locality = input("Enter locality: ")
    city = input("Enter city: ")
    pincode = int(input("Enter pincode: "))
    current_cart = int(input("Enter current cart: "))
    password = input("Enter password: ")

    # Insert customer data into the database
    cursor.execute("INSERT INTO Customer (Cust_ID, Name, Phone_No, Email, House_No, Locality, City, PinCode, Current_cart, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cust_id, name, phone_no, email, house_no, locality, city, pincode, current_cart, password))

    # Commit the changes
    server.commit()

    cursor.close()
    server.close()

    return

# Add trigger here...
def signIn():
    name = input("Enter name : ")
    pwd = input("Enter password : ")
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb", autocommit=True)
    cursor = server.cursor()
    query = "SELECT * FROM Customer WHERE Name = %s AND Password = %s"
    cursor.execute(query, (name, pwd))
    result = cursor.fetchall()
    current_cart = getCartID()
    if len(result) > 0:
        custID = result[0][0]
        cmd = "UPDATE customer SET Current_Cart = %s WHERE Cust_ID = %s"
        cursor.execute(cmd, (current_cart, custID,))
        print(custID)
        print("Sign in successful.")
    else:
        print("Sign in failed. Please check your name and password.")

    cursor.close()
    server.close()

    return


def showdatabases():
    try:
        db = conn.connect(host = "localhost", user = "root", password = admin)
        # print(3)
        MyCursor = db.cursor()
        sql = "show databases"
        MyCursor.execute(sql)
        for x in MyCursor:
            print(x)    
    except:
        print("Error in connection")



def searchProduct():
    try:
        server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb", autocommit=True)
        # print(2)
        # print("Connected to MySQL database!")
        cursor = server.cursor()
        item = input("Enter item name : ")
        cmd = "SELECT * FROM Product WHERE Name LIKE %s"
        cursor.execute(cmd, ('%' + item+ '%', ))

        result = cursor.fetchall()
        for row in result:
            print(row)


    except conn.Error as err:
        print("Unable to connect to server.")
        print(err)
        sys.exit(0)
    return


def addProduct():
    global custID
    if(custID != -1):
        try:
            server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb", autocommit=True)
            cursor = server.cursor()
            prod_id = int(input("Enter Product ID: "))
            cmd = "SELECT Quantity FROM Availability WHERE Prod_ID = %s"
            cursor.execute(cmd, (prod_id,))
            result = cursor.fetchall()
            count = result[0][0]
            quantity = int(input("Enter quantity: "))
            if (quantity > count or quantity < 0):
                print("Ordered Quantity not available")
            else:
                count = count - quantity
                cmd = "UPDATE Availability SET Quantity = %s WHERE Prod_ID = %s"
                cursor.execute(cmd,(count,prod_id,))
                cmd = "SELECT Current_Cart FROM customer where Cust_ID = %s"
                cursor.execute(cmd,(custID,))
                result = cursor.fetchall()
                cartID = result[0][0]
                cmd = "INSERT INTO added_products (Prod_ID, Quantity, Cart_ID) VALUES (%s, %s, %s)"
                cursor.execute(cmd, (prod_id, quantity, cartID,))

        except conn.Error as err:
            print("Unable to connect to server.")
            print(err)
            sys.exit(0)    
    else:
        print("Customer not signed in.")

def removeProduct():
    global custID
    if custID != -1:
        try:
            server = conn.connect(host="localhost", user="root", password=admin, database="zappiedb", autocommit=True)
            cursor = server.cursor()

            prod_id = int(input("Enter Product ID to remove: "))

            cmd = "SELECT * FROM added_products WHERE Prod_ID = %s AND Cart_ID = (SELECT Current_Cart FROM customer WHERE Cust_ID = %s)"
            cursor.execute(cmd, (prod_id, custID))
            result = cursor.fetchall()

            if not result:
                print("Product not found in the cart.")
                return

            cmd = "SELECT Quantity FROM added_products WHERE Prod_ID = %s AND Cart_ID = (SELECT Current_Cart FROM customer WHERE Cust_ID = %s)"
            cursor.execute(cmd, (prod_id, custID))
            quantity = cursor.fetchone()[0]

            cmd = "UPDATE Availability SET Quantity = Quantity + %s WHERE Prod_ID = %s"
            cursor.execute(cmd, (quantity, prod_id))

            cmd = "DELETE FROM added_products WHERE Prod_ID = %s AND Cart_ID = (SELECT Current_Cart FROM customer WHERE Cust_ID = %s)"
            cursor.execute(cmd, (prod_id, custID))

            print("Product removed successfully.")
        except conn.Error as err:
            print("Unable to connect to server.")
            print(err)
            sys.exit(0)
    else:
        print("Customer not signed in.")

def placeOrder():
    try:
        server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
        cursor = server.cursor()
        payment_mode = input("Enter preferred payment mode:")

        order_id = getOrdertID()
        placingdateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        DeliveryDateTime = None
        cart_id = getCartID()
        trans_id = getTransID()
        cust_id = getCustID()
        emp_id = selectRandomDeliveryPartner()

        cursor.execute("SELECT prod_ID, quantity FROM added_products WHERE cart_id = %s", (cart_id,))
        products_in_cart = cursor.fetchall()
        status = 'pending'
        total_amount = 0

        for product in products_in_cart:
            prod_id = product[0]
            quantity = product[1]

            cursor.execute("SELECT price FROM product WHERE prod_ID = %s", (prod_id,))
            price = cursor.fetchone()[0]

            product_amount = price * quantity

            total_amount += product_amount

        cursor.execute("INSERT INTO `Zappiedb`.`Order` (`Order_ID`, `PlacingDateTime`, `DeliveryDateTime`, `Amount`, `Status`, `Trans_ID`, `Cust_ID`, `Emp_ID`, `Cart_ID`, `PaymentMode`)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (order_id, placingdateTime, DeliveryDateTime, total_amount, status, trans_id, cust_id, emp_id, cart_id, payment_mode))

        server.commit()
        print("Order placed successfully!")
    except Exception as e:
        print("Error:", e)

    return

def getCartID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Cart_ID FROM cart"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)


def getCustID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Cust_ID FROM customer"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)

def getOrdertID():
    server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
    cursor = server.cursor()
    cmd = "SELECT Order_ID FROM Order"
    cursor.execute(cmd)
    result = cursor.fetchall()
    l = [i[0] for i in result]
    return(max(l) + 1)


def selectRandomDeliveryPartner(conn):
    try:
        server = conn.connect(host = "localhost", user = "root", password = admin, database = "zappiedb")
        cursor = conn.cursor()

        # Fetch all Emp_IDs from the DeliveryPartner table
        cursor.execute("SELECT Emp_ID FROM DeliveryPartner")
        emp_ids = cursor.fetchall()

        # If there are no delivery partners in the table, return None
        if not emp_ids:
            return None

        # Randomly select an Emp_ID from the list of Emp_IDs
        random_emp_id = random.choice(emp_ids)[0]

        cursor.close()

        return random_emp_id
    except Exception as e:
        print("Error:", e)
        return None


















# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def show_previous_orders(cust_id):
    db = conn.connect(host="localhost", user="root", password=admin, database="Zappiedb", autocommit=True)
    cursor = db.cursor()

    query = "SELECT * FROM `Order` WHERE Cust_ID = %s"
    cursor.execute(query, (cust_id,))
    orders = cursor.fetchall()

    if len(orders) == 0:
        print("No previous orders found.")
    else:
        for order in orders:
            print(f"Order ID: {order[0]}, Placing Date Time: {order[1]}, Delivery Date Time: {order[2]}, Status: {order[5]}")

    cursor.close()
    db.close()

def show_profile(cust_id):
    db = conn.connect(host="localhost", user="root", password=admin, database="Zappiedb", autocommit=True)
    cursor = db.cursor()

    query = "SELECT * FROM Customer WHERE Cust_ID = %s"
    cursor.execute(query, (cust_id,))
    customer = cursor.fetchone()

    print("Customer ID:", customer[0])
    print("Name:", customer[1])
    print("Phone Number:", customer[2])
    print("Email:", customer[3])
    print("House Number:", customer[4])
    print("Locality:", customer[5])
    print("City:", customer[6])
    print("Pincode:", customer[7])

    cursor.close()
    db.close()

def edit_profile(cust_id):
    db = conn.connect(host="localhost", user="root", password=admin, database="Zappiedb", autocommit=True)
    cursor = db.cursor()

    print("Choose an option to edit:")
    print("1. Change address")
    print("2. Change password")
    print("3. Go back to main menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            house_no = input("Enter new house number: ")
            locality = input("Enter new locality: ")
            city = input("Enter new city: ")
            pincode = input("Enter new pincode: ")
            cursor.execute("UPDATE Customer SET House_No = %s, Locality = %s, City = %s, PinCode = %s WHERE Cust_ID = %s", (house_no, locality, city, pincode, cust_id))
            print("Address updated successfully.")
        elif choice == "2":
            password = input("Enter new password: ")
            cursor.execute("UPDATE Customer SET Password = %s WHERE Cust_ID = %s", (password, cust_id))
            print("Password updated successfully.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    db.commit()
    cursor.close()
    db.close()

def menuForCustomerAnalysis():
    while True:
        print("\nMenu:")
        print("1. View previous orders")
        print("2. Show profile")
        print("3. Edit profile")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_previous_orders(custID)
        elif choice == "2":
            show_profile(custID)
        elif choice == "3":
            edit_profile(custID)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")




# print(1)
# showdatabases()
# signIn()
# searchProduct()
# addProduct()
#print(getCustID())
