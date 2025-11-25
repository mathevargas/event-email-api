from pydantic import BaseModel, EmailStr

class EnviarEmailDTO(BaseModel):
    remetente: EmailStr
    destinatario: EmailStr
    assunto: str
    mensagem: str
