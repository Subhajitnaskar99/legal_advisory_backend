from app.database import users_collection
from bson import ObjectId
from datetime import datetime

async def get_user_by_email(email: str):
    return await users_collection.find_one({"email": email})

async def create_user(email: str, full_name: str | None = None, role: str = "client"):
    doc = {"email": email, "full_name": full_name, "role": role, "created_at": datetime.utcnow()}
    res = await users_collection.insert_one(doc)
    doc["_id"] = str(res.inserted_id)
    return doc

async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})
