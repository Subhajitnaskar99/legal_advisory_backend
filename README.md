# legal_advisory_backend
Legal advisory application APIs

API-1 
Method POST
http://localhost:8000/auth/send_email_code
sample request: {
    "email":"subhajitnaskar99@gmail.com"
}
reponse : {
    "status": "ok",
    "message": "Verification code sent"
}

API 2:
method : POST
url : http://localhost:8000/auth/verify_email_code
Request: {
    "email":"subhajitnaskar99@gmail.com",
    "code":"891047"
}

Test
    	
Response body
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OGZiNDU1M2EyZmFmNGU4YjVhZTFlMTAiLCJpYXQiOjE3NjEyOTc3NDcsImV4cCI6MTc2MTI5ODY0NywiZW1haWwiOiJzdWJoYWppdEBnbWFpbC5jb20ifQ.zfZIrVhmD1sNFzCtUe2tI5TV4oWgzWWjgrXMWFVWXE4",
  "token_type": "bearer",
  "already_user": false,
  "full_name": null
}


API 3:

method : PUT
url : http://localhost:8000/users/update_basic_info
Authorization : Bearer <JWT Token >

request : {
  "email": "subhajit@example.com",
  "full_name": "Subhajit naskar",
  "role": "client",
  "phone": "8981122182",
  "address": {
    "house_no": "123",
    "street": "Main Street",
    "city": "Kolkata",
    "state": "WB",
    "pin_code": "700001",
    "country": "India"
  }
}

response: {
    "status": "success",
    "message": "User details updated successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OGVhYzIwYzYwMGVhZWE1YTUyMjQ3YjQiLCJpYXQiOjE3NjAyOTU1ODEsImV4cCI6MTc2MDI5NjQ4MSwiZW1haWwiOiJzdWJoYWppdG5hc2thcjk5QGdtYWlsLmNvbSJ9.YWKhjCMBbxXg8-U_YbbZbCRakDkulqi-eyg-CzA8DNs"
}

API 4:
method : GET
URL for the Get method: http://localhost:8000/users/me
Bearer Token type : Authorization Header is Token
Sample request : BODY is null

Sample response : 

{
    "status": "success",
    "message": "User details updated successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OGVkZjA0YjUwMjg1ODZmYmRiNTk3NTIiLCJpYXQiOjE3NjA0MzAzMzksImV4cCI6MTc2MDQzMTIzOSwiZW1haWwiOiJzdWJoYWppdG5hc2thcjk5QGdtYWlsLmNvbSJ9.zGDWht-8ajh3S9JDPjSNMCQ2gQIRLNQFRza2-p8MpFI",
    "email": "subhajitnaskar99@gmail.com",
    "full_name": "Subhajit naskar",
    "role": "client",
    "phone": "8981122182",
    "address": {
        "street": "Main Street",
        "city": "Kolkata",
        "state": "WB",
        "pin_code": "700001",
        "country": "India"
    },
    "dob": null,
    "gender": null
}

API 5:


