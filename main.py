import pyodbc

@app.get("/sales")
def get_sales():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=jaywant-sql-server.database.windows.net;"
        "DATABASE=PowerBIJaywantDB;"
        "UID=jaywantadmin;"
        "PWD=Bykorani@2026;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    cursor = conn.cursor()

    query = """
    SELECT SUM(TotalDue) AS total_sales
    FROM Sales.SalesOrderHeader
    """

    cursor.execute(query)
    row = cursor.fetchone()

    conn.close()

    return {
        "total_sales": float(row[0]),
        "insight": "Live data from Azure SQL 🚀"
    }