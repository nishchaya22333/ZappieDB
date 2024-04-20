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