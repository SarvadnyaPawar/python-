import mysql.connector

# Create connection
conn = mysql.connector.connect(
    host="localhost",        # or your MySQL server IP
    user="root",    # e.g., "root"
    password="",
    database="test" # optional, if you want to connect to a specific database
)

# Check if connection is successful
if conn.is_connected():
    print("Connected to MySQL database")

# Close the connection
conn.close()
