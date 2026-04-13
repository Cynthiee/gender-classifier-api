from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
import httpx


app = FastAPI()

@app.get("/api/classify")
async def classify(name: str = None):
    # Check if name is missing or empty
    if not name or name.strip() == "":
        return JSONResponse(
            status_code=400,
            content={ "status": "error", "message": "No prediction available for the provided name" }
        )
    
    # Call Genderize API
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.genderize.io?name={name.strip()}")
        api_data = response.json()
    if not api_data["gender"] or api_data["count"] == 0:
        return JSONResponse(
        status_code=200,
        content={"status": "error", "message": "No prediction available for the provided name"}
        )

    # Extract values from Genderize response
    gender = api_data["gender"]
    probability = api_data["probability"]
    sample_size = api_data["count"]

    # Calculate is_confident
    is_confident = probability >= 0.7 and sample_size >= 100
    processed_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  #Displays time

    # Return processed response
    return {
        "status": "success",
        "data":{
        "name": name.strip(),
        "gender": gender,
        "probability": probability,
        "sample_size": sample_size,
        "is_confident": is_confident,
        "processed_at": processed_at
        }
    }