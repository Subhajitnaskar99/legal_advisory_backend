from pydantic import BaseModel, EmailStr

class SendEmailCodeIn(BaseModel):
    email: EmailStr

class VerifyEmailCodeIn(BaseModel):
    email: EmailStr
    code: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
