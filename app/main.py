from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, email_otp, advocates
from app.database import email_otps_collection, refresh_tokens_collection, advocates_collection
from pymongo import GEOSPHERE

app = FastAPI(title="Legal Advisory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(email_otp.router)
app.include_router(advocates.router)

@app.on_event("startup")
async def startup():
    await email_otps_collection.create_index("expire_at", expireAfterSeconds=0)
    await refresh_tokens_collection.create_index("expires_at", expireAfterSeconds=0)
    await advocates_collection.create_index([("location", GEOSPHERE)])