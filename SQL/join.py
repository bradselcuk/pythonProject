import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=SatisVT;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
cursor.execute("SELECT KATEGORIAD,COUNT(*) FROM TBLURUNLER INNER JOIN TBLKATEGORI ON TBLURUNLER.KATEGORI=TBLKATEGORI.KATEGORIID GROUP BY KATEGORIAD")

for x in cursor:
    print(x)

conn.close()