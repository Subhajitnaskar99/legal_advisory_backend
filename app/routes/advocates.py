from fastapi import APIRouter, HTTPException, Query
from bson import ObjectId
from app.database import advocates_collection
from ..models.location import Advocate
from ..models.location import Location

router = APIRouter(prefix="/advocate", tags=["advocate"])

@router.post("/add")
async def add_advocate(advocate: Advocate):
    result = await advocates_collection.insert_one(advocate.dict())
    return {"id": str(result.inserted_id)}

@router.get("/nearby")
async def get_nearby_advocate(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    max_distance: int = Query(5000, description="Max distance in meters")
):
    doctors = await advocates_collection.aggregate([
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [lon, lat]},
                "distanceField": "distance",
                "maxDistance": max_distance,
                "spherical": True
            }
        }
    ]).to_list(20)

    return [{"name": d["name"], "specialization": d["specialization"], "distance": round(d["distance"], 2)} for d in doctors]
