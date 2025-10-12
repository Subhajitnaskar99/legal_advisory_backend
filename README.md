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
response : {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OGVhYzIwYzYwMGVhZWE1YTUyMjQ3YjQiLCJpYXQiOjE3NjAyOTU1ODEsImV4cCI6MTc2MDI5NjQ4MSwiZW1haWwiOiJzdWJoYWppdG5hc2thcjk5QGdtYWlsLmNvbSJ9.YWKhjCMBbxXg8-U_YbbZbCRakDkulqi-eyg-CzA8DNs",
    "token_type": "bearer"
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



