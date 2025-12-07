from app.dtos.enviar_email_dto import EnviarEmailDTO
from app.utils.template_utils import TemplateUtils


class HtmlEmailService:

    @staticmethod
    def gerar_email_html(dto: EnviarEmailDTO) -> str:
        """
        Gera HTML final usando o template padrão (email_base.html)
        """

        return TemplateUtils.render(
            "email_base.html",
            nome="Participante",
            assunto=dto.assunto,
            mensagem=dto.mensagem
        )
