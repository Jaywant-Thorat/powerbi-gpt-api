from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()


# 🔌 DATABASE CONNECTION FUNCTION
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


# ✅ BASIC SALES API (STATIC)
@app.get("/sales")
def get_sales_data(
    region: str = Query(None),
    min_sales: float = Query(None)
):
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
    result = cursor.fetchone()[0]

    conn.close()

    return {
        "total_sales": result
    }


# 🚀 DYNAMIC SALES API (NEXT LEVEL)
@app.get("/dynamic-sales")
def dynamic_sales(
    region: str = Query(None),
    min_sales: float = Query(None)
):
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
    result = cursor.fetchone()[0]

    conn.close()

    return {
        "query_used": query,
        "parameters": params,
        "total_sales": result
    }


# 🏠 ROOT ENDPOINT (OPTIONAL - avoids 404 confusion)
@app.get("/")
def root():
    return {
        "message": "Power BI GPT API is running 🚀"
    }