from dataclasses import dataclass

@dataclass
class EmailModel:
    destinatario: str
    assunto: str
    mensagem: str
