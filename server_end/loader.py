import sys
import mysql.connector

server = 0
def createDatabase(server):
    cursor = server.cursor()
    with open("db_creation.sql", "r") as sql_file:
        sql_queries = sql_file.read()
    queries = sql_queries.split(";")
    try:
        # Execute each SQL query
        for query in queries:
            if query.strip():  # Skip empty queries
                cursor.execute(query)

        print("Database Creation Successful")
        return(True)
    except mysql.connector.Error as err:
        print("Error while loading the database:", err)
        return(False)
    finally:
        cursor.close()

def updateDatabaseModification(server):
    cursor = server.cursor()
    with open("db_modifications.sql", "r") as sql_file:
        sql_queries = sql_file.read()
    queries = sql_queries.split(";")
    try:
        # Execute each SQL query
        for query in queries:
            if query.strip():  # Skip empty queries
                cursor.execute(query)

        print("Modifications Done Successfully")
        return(True)
    except mysql.connector.Error as err:
        print("Error while modifying the database:", err)
        return(False)
    finally:
        cursor.close()

def insertData(server):
    cursor = server.cursor()
    with open("data_insertion.sql", "r") as sql_file:
        sql_queries = sql_file.read()
    queries = sql_queries.split(";")
    try:
        # Execute each SQL query
        for query in queries:
            if query.strip():  # Skip empty queries
                cursor.execute(query)

        print("Insertions Done Successfully")
        return(True)
    except mysql.connector.Error as err:
        print("Error while inserting data:", err)
        return(False)
    finally:
        cursor.close()

def load(server):
    r = createDatabase(server)
    if (r):
        r = updateDatabaseModification(server)
    if (r):
        r = insertData(server)
    return r


def connectServer(host, username, password):
    global server
    try:
        server = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            autocommit=True
        )
        return(True)
    except mysql.connector.Error as err:
        return(False)

def getServer():
    global server
    return server

def cliConnect():
    host = input("Host: ")
    username = input("Username: ")
    password = input("Password: ")

    try:
        server = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            autocommit=True
        )
        print("Connected to MySQL database!")
    except mysql.connector.Error as err:
        print("Unable to connect to server.")
        print(err)
        sys.exit(0)

    createDatabase(server)
    updateDatabaseModification(server)
    insertData(server)

    return server
