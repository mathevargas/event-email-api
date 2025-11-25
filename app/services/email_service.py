from app.models.email_model import EmailModel

class EmailService:

    def enviar_email(self, dto):
        """
        Serviço simples que "envia" um email (simulação).
        """

        email = EmailModel(
            remetente=dto.remetente,
            destinatario=dto.destinatario,
            assunto=dto.assunto,
            mensagem=dto.mensagem
        )

        # Aqui futuramente chamaremos SMTP ou API real
        return {
            "status": "enviado",
            "para": email.destinatario,
            "assunto": email.assunto,
            "mensagem": email.mensagem
        }
