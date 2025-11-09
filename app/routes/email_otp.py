import os, secrets, hashlib, hmac, time
from datetime import datetime, timedelta
import aiosmtplib
from email.message import EmailMessage
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, HTTPException , APIRouter
from pydantic import BaseModel, EmailStr
import jwt as pyjwt
from dotenv import load_dotenv
from app.config import settings
from app.database import email_otps_collection, users_collection
from app.security.jwt import create_access_token, decode_token
load_dotenv()

router = APIRouter(prefix="/auth", tags=["auth"])
# --------------------------------------------------------------------
# Models
# --------------------------------------------------------------------
class SendEmailIn(BaseModel):
    email: EmailStr


class VerifyEmailIn(BaseModel):
    email: EmailStr
    code: str
async def send_email(to: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = os.getenv("FROM_EMAIL")
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        await aiosmtplib.send(
            msg,
            hostname=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT", 587)),
            start_tls=True,
            username=os.getenv("SMTP_USER"),
            password=os.getenv("SMTP_PASS"),
        )
        print(f"📧 Email sent to {to}")
    except Exception as e:
        print(f"❌ Unable to send email: {e}")
        raise HTTPException(status_code=500, detail="Email sending failed.")
@router.post("/send_email_code")
async def send_email_code(payload: SendEmailIn):
    code = "".join(secrets.choice("0123456789") for _ in range(6))
    print(f"Generated code for {payload.email}: {code}")
    salt = secrets.token_urlsafe(8)
    code_hash = hmac.new(salt.encode(), code.encode(), hashlib.sha256).hexdigest()
    expire_at = datetime.utcnow() + timedelta(minutes=5)

    await email_otps_collection.insert_one(
        {"email": payload.email, "hash": code_hash, "salt": salt, "expire_at": expire_at}
    )
    body = f"Your verification code for LegalAdvisory is {code}. It expires in 5 minutes."
    await send_email(payload.email, "LegalAdvisory – Verify Your Email", body)
    return {"status": "ok", "message": "Verification code sent"}


@router.post("/verify_email_code")
async def verify_email_code(payload: VerifyEmailIn):
    doc = await email_otps_collection.find_one({"email": payload.email})
    if not doc:
        raise HTTPException(status_code=400, detail="No code sent.")
    if datetime.utcnow() > doc["expire_at"]:
        raise HTTPException(status_code=400, detail="Code expired.")

    expected = hmac.new(doc["salt"].encode(), payload.code.encode(), hashlib.sha256).hexdigest()
    if not secrets.compare_digest(expected, doc["hash"]):
        raise HTTPException(status_code=400, detail="Invalid code.")

    await email_otps_collection.delete_one({"_id": doc["_id"]})
    user = await users_collection.find_one({"email": payload.email})
    full_name = user.get("full_name") if user else None
    if not user:
        res = await users_collection.insert_one({"email": payload.email, "created_at": datetime.utcnow()})
        user_id = str(res.inserted_id)
        already_user = False
    else:
        user_id = str(user["_id"])
        already_user = True

    token = create_access_token(subject=user_id, extra={"email": payload.email})
    print (decode_token(token))
    return {"access_token": token, "token_type": "bearer", "already_user": already_user,
            "full_name": full_name}
