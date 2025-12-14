import re
from app.dtos.enviar_email_dto import EnviarEmailDTO
from app.models.email_model import EmailModel
from app.utils.template_utils import TemplateUtils
from app.services.smtp_service import SMTPService


def _looks_like_html(s: str) -> bool:
    if not s:
        return False
    return bool(re.search(r"<\s*\/?\s*[a-zA-Z][^>]*>", s))


def _extrair_evento(texto: str) -> str | None:
    if not texto:
        return None

    m = re.search(r"evento[:\s]+(.+)$", texto, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().strip(".").strip('"').strip("“”")

    m2 = re.search(r"<strong>\s*(.*?)\s*</strong>", texto, flags=re.IGNORECASE)
    if m2:
        return m2.group(1).strip()

    return None


def _tipo_email(assunto: str, mensagem: str) -> str:
    a = (assunto or "").lower()
    m = (mensagem or "").lower()

    if "cancel" in a or "cancel" in m:
        return "cancelamento"

    if "check" in a or "check-in" in a or "checkin" in a or "check" in m or "check-in" in m or "checkin" in m:
        return "checkin"

    if "inscri" in a or "inscri" in m:
        return "inscricao"

    return "generico"


class EmailService:

    def enviar_email(self, dto: EnviarEmailDTO):
        msg = dto.mensagem or ""
        is_html = _looks_like_html(msg)

        email = EmailModel(
            destinatario=dto.destinatario,
            assunto=dto.assunto,
            mensagem=msg
        )

        SMTPService.enviar(
            destinatario=email.destinatario,
            assunto=email.assunto,
            conteudo=email.mensagem,
            html=is_html
        )

        return {"status": "ok", "tipo": "html" if is_html else "texto", "destinatario": email.destinatario}

    def enviar_email_html(self, dto: EnviarEmailDTO):

        assunto = dto.assunto or ""
        msg = dto.mensagem or ""

        if _looks_like_html(msg):
            html_final = msg

        else:
            tipo = _tipo_email(assunto, msg)
            evento = _extrair_evento(msg) or "seu evento"
            nome = "Participante"

            if tipo == "inscricao":
                html_final = TemplateUtils.render(
                    "inscricao_confirmada.html",
                    nome=nome,
                    evento=evento
                )

            elif tipo == "checkin":
                html_final = TemplateUtils.render(
                    "checkin_confirmado.html",
                    nome=nome,
                    evento=evento
                )

            elif tipo == "cancelamento":
                html_final = TemplateUtils.render(
                    "cancelamento_inscricao.html",
                    nome=nome,
                    evento=evento
                )

            else:
                html_final = TemplateUtils.render(
                    "email_template.html",
                    nome=nome,
                    assunto=assunto,
                    mensagem=msg
                )

        email = EmailModel(
            destinatario=dto.destinatario,
            assunto=assunto,
            mensagem=html_final
        )

        SMTPService.enviar(
            destinatario=email.destinatario,
            assunto=email.assunto,
            conteudo=email.mensagem,
            html=True
        )

        return {"status": "ok", "tipo": "html", "destinatario": email.destinatario}
