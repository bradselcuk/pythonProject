import pyodbc
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
cursor.execute("")
 
conn.close()