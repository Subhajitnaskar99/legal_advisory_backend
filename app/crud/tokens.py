from app.database import refresh_tokens_collection
from app.utils.hashing import hash_token
from datetime import datetime

async def store_refresh_token(user_id: str, refresh_token: str, expires_at: datetime):
    hashed = hash_token(refresh_token)
    await refresh_tokens_collection.insert_one({
        "user_id": user_id,
        "token_hash": hashed,
        "expires_at": expires_at,
        "created_at": datetime.utcnow()
    })
