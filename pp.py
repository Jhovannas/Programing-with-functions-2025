import pymysql

# Replace with your MySQL database details
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="sakila"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")

print("Tables in the database:")
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()

