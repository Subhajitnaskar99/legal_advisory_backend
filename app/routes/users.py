from fastapi import APIRouter, Depends, HTTPException, Header
from app.security.deps import get_current_user
from app.models.user import UserPublic, UserDetails
from app.security.jwt import decode_token
from app.database import users_collection
from app.config import settings
from bson.objectid import ObjectId
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserPublic)
async def get_me(user = Depends(get_current_user)):
    return {"email": user["email"], "full_name": user.get("full_name"), "role": user.get("role")}

@router.put("/update_basic_info")
async def update_basic_info(
    user: UserDetails,
    authorization: str = Header(...)
):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token payload")

    db_user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    update_fields = {k: v for k, v in user.dict().items() if v is not None}

    await users_collection.update_one(
        {"_id": ObjectId(user_id), "email": db_user["email"]},
        {"$set": update_fields}
    )

    return {
        "status": "success",
        "message": "User details updated successfully",
        "token": token
    }
