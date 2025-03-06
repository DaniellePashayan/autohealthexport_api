from fastapi import FastAPI, Request, HTTPException, Header
from typing import Optional
import os

app = FastAPI()

@app.get("/api/get_data")
async def get_data():
    return {"data": "Some data"}

@app.post("/api/import_data")
async def import_data(request: Request):
    try:
        data = await request.json()
        message = f"Received data: {data}"
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3111)