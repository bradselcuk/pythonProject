import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=PPP;"
    "Trusted_Connection=yes;"
)

print("Opened database successfully")

conn.execute("CREATE TABLE COMPANY (ID INT PRIMARY KEY     NOT NULL, NAME           TEXT    NOT NULL, AGE            INT     NOT NULL, ADDRESS        CHAR(50), SALARY         REAL)")
conn.commit()
print("Table created successfully")

conn.close()