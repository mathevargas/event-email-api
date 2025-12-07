from fastapi import FastAPI
from app.controllers.email_controller import router as email_router

app = FastAPI(
    title="Email API",
    version="1.0.0",
    description="Microserviço de envio de e-mails."
)

app.include_router(email_router)

@app.get("/")
def root():
    return {"message": "Email API is running!"}
