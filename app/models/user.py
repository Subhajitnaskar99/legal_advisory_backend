from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pin_code: str # Mandatory
    country: Optional[str] = None

class UserDetails(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: str = "client" or "admin" or "lawyer"
    dob: Optional[datetime] = None
    phone: Optional[str] = None
    address : Address
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserPublic(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: str
