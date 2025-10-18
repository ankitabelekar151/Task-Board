# app/test_db.py
import asyncio
from app.db import db

async def test_connection():
    try:
        # List database names
        databases = await db.client.list_database_names()
        print("Connected successfully! Databases:", databases)
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())
