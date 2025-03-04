from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.post("/api/import_data")
async def process_data(request: Request):
    try:
        data = await request.json()  # Get raw JSON data
        message = f"Received data: {data}"
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)