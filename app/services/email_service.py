from app.dtos.enviar_email_dto import EnviarEmailDTO
from app.models.email_model import EmailModel
from app.utils.template_utils import TemplateUtils
from app.services.smtp_service import SMTPService


class EmailService:

    def enviar_email(self, dto: EnviarEmailDTO):

        email = EmailModel(
            destinatario=dto.destinatario,
            assunto=dto.assunto,
            mensagem=dto.mensagem
        )

        SMTPService.enviar(
            destinatario=email.destinatario,
            assunto=email.assunto,
            conteudo=email.mensagem,
            html=False
        )

        return {
            "status": "ok",
            "tipo": "texto",
            "destinatario": email.destinatario
        }

    def enviar_email_html(self, dto: EnviarEmailDTO):

        html = TemplateUtils.render(
            "email_template.html",
            nome="Participante",
            assunto=dto.assunto,
            mensagem=dto.mensagem
        )

        email = EmailModel(
            destinatario=dto.destinatario,
            assunto=dto.assunto,
            mensagem=html
        )

        SMTPService.enviar(
            destinatario=email.destinatario,
            assunto=email.assunto,
            conteudo=email.mensagem,
            html=True
        )

        return {
            "status": "ok",
            "tipo": "html",
            "destinatario": email.destinatario
        }
