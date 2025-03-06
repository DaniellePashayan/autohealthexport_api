from fastapi import FastAPI, Request, HTTPException, Header
from typing import Optional
import os

app = FastAPI()

API_KEY = os.environ.get("API_KEY")  # Get API key from environment variable

async def verify_api_key(api_key: Optional[str] = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.post("/api/import_data")
async def import_data(request: Request, api_key: Optional[str] = Header(None)):
    await verify_api_key(api_key)  # Verify API key

    try:
        data = await request.json()
        message = f"Received data: {data}"
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3111)