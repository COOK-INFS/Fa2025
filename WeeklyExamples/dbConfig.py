import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user='infs3070',
        password='pydev',
        database='INFS3070'
    )
    return conn