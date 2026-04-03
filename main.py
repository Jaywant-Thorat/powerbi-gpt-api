from fastapi import FastAPI
import pyodbc

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Power BI API running on Azure SQL 🚀"}

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
        "total_sales": float(row[0]) if row[0] else 0,
        "insight": "Live data from Azure SQL 🚀"
    }