from fastapi import APIRouter, Depends, HTTPException, status
from app.dtos.enviar_email_dto import EnviarEmailDTO
from app.services.email_service import EmailService
from app.security.deps import auth_required

router = APIRouter(prefix="/emails", tags=["Emails"])

service = EmailService()


@router.post("/enviar", dependencies=[Depends(auth_required)])
def enviar_email(data: EnviarEmailDTO):
    return service.enviar_email(data)


@router.post("/enviar-html", dependencies=[Depends(auth_required)])
def enviar_email_html(data: EnviarEmailDTO):
    return service.enviar_email_html(data)
