from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

users_collection = db["users"]
refresh_tokens_collection = db["refresh_tokens"]
email_otps_collection = db["email_otps"]
verifications = db["verifications"]
