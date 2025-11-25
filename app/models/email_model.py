class EmailModel:
    def __init__(self, remetente: str, destinatario: str, assunto: str, mensagem: str):
        self.remetente = remetente
        self.destinatario = destinatario
        self.assunto = assunto
        self.mensagem = mensagem
