from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from pymongo import GEOSPHERE

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

users_collection = db["users"]
refresh_tokens_collection = db["refresh_tokens"]
email_otps_collection = db["email_otps"]
advocates_collection = db["advocates"]
# Ensure geospatial index on advocates collection
async def init_indexes():
    await advocates_collection.create_index([("location", GEOSPHERE)])

