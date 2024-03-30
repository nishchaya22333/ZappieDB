import sys
import mysql.connector

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
    except mysql.connector.Error as err:
        print("Error while loading the database:", err)
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
    except mysql.connector.Error as err:
        print("Error while modifying the database:", err)
    finally:
        cursor.close()

def load():
    host = input("Host: ")
    username = input("Username: ")
    password = input("Password: ")

    try:
        server = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )
        print("Connected to MySQL database!")
    except mysql.connector.Error as err:
        print("Unable to connect to server.")
        print(err)
        sys.exit(0)

    createDatabase(server)
    updateDatabaseModification(server)

    return server