import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="128.198.162.191", # IP Address of class Production server.
        user='infs3070',
        password='fa2025', # Check Canvas for updated password.
        database='INFS3070',
        auth_plugin='mysql_native_password', # Explicity specifies the authentication plugin.
        use_pure=True
    )
    return conn