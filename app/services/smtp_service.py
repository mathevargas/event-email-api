import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class SMTPService:

    HOST = "smtp.gmail.com"
    PORT = 465  

    @staticmethod
    def enviar(destinatario: str, assunto: str, conteudo: str, html: bool = False):
        
        user = os.getenv("EMAIL_API_USER", "").replace('"', '').strip()
        password = os.getenv("EMAIL_API_PASS", "").replace('"', '').strip()

        if not user or not password:
            raise Exception("EMAIL_API_USER ou EMAIL_API_PASS não configurados no .env")

        msg = MIMEMultipart("alternative")
        msg["Subject"] = assunto
        msg["From"] = user
        msg["To"] = destinatario

        body = MIMEText(conteudo, "html" if html else "plain")
        msg.attach(body)

        try:
            with smtplib.SMTP_SSL(SMTPService.HOST, SMTPService.PORT) as server:
                server.login(user, password)
                server.sendmail(user, destinatario, msg.as_string())
        except Exception as e:
            raise Exception(f"Erro SMTP: {str(e)}")
