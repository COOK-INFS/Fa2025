import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user='infs3070',
        password='pydev',
        database='infs3070'
    )
    return conn