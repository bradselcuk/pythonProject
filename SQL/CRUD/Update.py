import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=PPP;"
    "Trusted_Connection=yes;"
)
print("Opened database successfully")
print(" ")
conn.execute("UPDATE COMPANY set SALARY = 25000 where ID = 1")
conn.commit()

print("Operation done successfully")
conn.close()




