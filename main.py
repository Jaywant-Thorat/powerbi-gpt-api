from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()


# 🔌 DATABASE CONNECTION
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


# 🛡️ SAFE RESULT HANDLER
def safe_fetch(cursor):
    row = cursor.fetchone()
    if row and row[0] is not None:
        return float(row[0])
    return 0


# ✅ BASIC SALES API
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

    result = safe_fetch(cursor)

    conn.close()

    return {
        "total_sales": result
    }


# 🚀 DYNAMIC SALES API
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

    result = safe_fetch(cursor)

    conn.close()

    return {
        "query_used": query,
        "parameters": params,
        "total_sales": result
    }


# 🏠 ROOT ENDPOINT (for health check)
@app.get("/")
def root():
    return {
        "message": "Power BI GPT API is running 🚀"
    }