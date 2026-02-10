from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from db import get_db
from utils.email_sender import send_email

router=APIRouter()

@router.post("/send-email")
def send_email_route(email:str,content:str,subject:str,db:session = Depends(get_db)):
    """ send an email to the receiver with the given subject and content."""
    send_email(email,content,subject)
    return {"message":"Email sent successfully"}