from fastapi import APIRouter
from app.dtos.enviar_email_dto import EnviarEmailDTO
from app.services.email_service import EmailService

router = APIRouter(prefix="/emails", tags=["Emails"])

service = EmailService()


@router.post("/enviar")
def enviar_email(data: EnviarEmailDTO):
    """
    Envia um email simples usando remetente, destinatário, assunto e mensagem.
    """
    return service.enviar_email(data)
