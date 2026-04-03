from fastapi import FastAPI
import os

app = FastAPI()

port = int(os.environ.get("PORT", 8000))

@app.get("/")
def home():
    return {"message": "Welcome to Power BI with Jaywant API 🚀"}

@app.get("/sales")
def get_sales():
    return {
        "total_sales": 100000,
        "region": "Bharat",
        "insight": "Sales are growing steadily"
    }