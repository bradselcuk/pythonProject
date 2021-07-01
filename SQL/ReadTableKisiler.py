import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=kitaplik;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
cursor.execute("SELECT * from kisiler")
for row in cursor:
    print(row)

conn.close()