from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()


def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=jaywant-sql-server.database.windows.net;"
        "DATABASE=PowerBIJaywantDB;"
        "UID=jaywantadmin;"
        "PWD=Bykorani@2026;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )


@app.get("/dynamic-sales")
def dynamic_sales(
    region: str = Query(None),
    min_sales: float = Query(None)
):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT SUM(SalesAmount) FROM Sales WHERE 1=1"
        params = []

        if region:
            query += " AND Region = ?"
            params.append(region)

        if min_sales:
            query += " AND SalesAmount >= ?"
            params.append(min_sales)

        cursor.execute(query, params)

        row = cursor.fetchone()

        result = 0
        if row is not None and len(row) > 0 and row[0] is not None:
            result = float(row[0])

        conn.close()

        return {
            "query_used": query,
            "parameters": params,
            "total_sales": result
        }

    except Exception as e:
        return {
            "error": str(e),
            "type": "debug"
        }


@app.get("/")
def root():
    return {"message": "API running 🚀"}