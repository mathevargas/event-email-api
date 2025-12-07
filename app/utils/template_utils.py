import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class TemplateUtils:

    @staticmethod
    def _templates_dir() -> str:
        """
        Retorna o caminho absoluto da pasta /templates.
        """
        base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        return os.path.join(base, "templates")

    @staticmethod
    def render(template: str, **kwargs) -> str:
        """
        Renderiza QUALQUER template da pasta /templates.

        Exemplo:
            TemplateUtils.render("email_inscricao.html", nome="Enzo", evento="Dev Summit")

        Caso o template não exista, retorna mensagem amigável.
        """
        try:
            env = Environment(
                loader=FileSystemLoader(TemplateUtils._templates_dir()),
                autoescape=True,
            )
            tpl = env.get_template(template)
            return tpl.render(**kwargs)

        except TemplateNotFound:
            return f"<p>Template '{template}' não encontrado.</p>"
