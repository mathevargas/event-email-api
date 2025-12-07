from pydantic import BaseModel, EmailStr

class EnviarEmailDTO(BaseModel):
    destinatario: EmailStr
    assunto: str
    mensagem: str
