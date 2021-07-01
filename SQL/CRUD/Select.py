import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=PPP;"
    "Trusted_Connection=yes;"
)
print("Opened database successfully")
print(" ")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

# for row in cursor:  #2.way
#     print(row)

for x in cursor:
    print("ID= ", x[0])
    print("NAME = ", x[1])
    print("ADDRESS = ", x[2])
    print("SALARY = ", x[3])

print(" ")
print("Operation done successfully")
conn.close()