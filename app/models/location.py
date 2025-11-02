from pydantic import BaseModel, Field
from typing import Optional, List

class Location(BaseModel):
    type: str = "Point"
    coordinates: List[float]  # [longitude, latitude]

class Advocate(BaseModel):
    id: Optional[str]= None
    name: str
    specialization: str
    address: str
    location: Location
    rating: float = 0.0