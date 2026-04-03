from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()

@app.get("/sales")
def get_sales(region: str = None, min_sales: float = 0):
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=jaywant-sql-server.database.windows.net;"
            "DATABASE=PowerBIJaywantDB;"
            "UID=jaywantadmin;"
            "PWD=Bykorani@2026;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
        )

        cursor = conn.cursor()

        query = "SELECT SUM(total_sales) FROM SalesData WHERE 1=1"
        params = []

        if region:
            query += " AND region = ?"
            params.append(region)

        if min_sales > 0:
            query += " AND total_sales >= ?"
            params.append(min_sales)

        cursor.execute(query, params)
        row = cursor.fetchone()

        conn.close()

        return {
            "total_sales": float(row[0]) if row[0] else 0
        }

    except Exception as e:
        return {"error": str(e)}