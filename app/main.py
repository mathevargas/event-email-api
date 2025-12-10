from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.email_controller import router as email_router
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="Email API",
    version="1.0.0",
    description="Microserviço de envio de e-mails."
)

# 🔓 CORS liberado para Portais e outras APIs
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

# ⬇️ Primeiro inclui as rotas
app.include_router(email_router)


@app.get("/")
def root():
    return {"message": "Email API is running!"}


# 🔐 Swagger com suporte a BearerAuth (JWT)
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
        "bearerFormat": "JWT"
    }

    # 🔒 Exige Auth por padrão em todas rotas (pode sobrescrever no controller)
    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# ⬅️ Substitui OpenAPI
app.openapi = custom_openapi
