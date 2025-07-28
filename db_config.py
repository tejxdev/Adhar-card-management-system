import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="programmer@123",
        database="aadhaar_db"
    )