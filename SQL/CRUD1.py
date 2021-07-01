import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=kitaplik;"
    "Trusted_Connection=yes;"
)
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from kitap")
    for row in cursor:
        print(f'row = {row}')
    print()


read(conn)
conn.close()
