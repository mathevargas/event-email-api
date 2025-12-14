from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.email_controller import router as email_router
from fastapi.openapi.utils import get_openapi
import time

app = FastAPI(
    title="EMAIL API",
    version="1.0.0",
    description="Microserviço de envio de e-mails do Sistema de Eventos.",
)

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
    "http://localhost:8003",
    "http://localhost:8004",
    "http://127.0.0.1:8004",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()

    metodo = request.method
    uri = request.url.path
    ip = request.client.host if request.client else None

    print(f"📌 LOG API → {metodo} {uri} | IP: {ip}")

    response = await call_next(request)

    ms = int((time.time() - start) * 1000)
    print(f"✅ RES API → {metodo} {uri} | status: {response.status_code} | {ms}ms")

    return response

app.include_router(email_router)


@app.get("/")
def root():
    return {"message": "Email API is running!"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema.setdefault("components", {})
    openapi_schema["components"].setdefault("securitySchemes", {})

    openapi_schema["components"]["securitySchemes"]["BearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }

    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
