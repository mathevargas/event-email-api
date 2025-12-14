EMAIL API — Serviço de Notificações por E-mail (HTML Templates + SMTP) — Python + FastAPI

Este microserviço é responsável por enviar e-mails reais do Sistema de Eventos via SMTP, suportando envio em texto e em HTML com templates (Jinja2).
Ele é acionado principalmente pelo backend (ex.: Events API) para notificar ações como inscrição, cancelamento e check-in/presença.

1) Objetivo

Disponibilizar um serviço centralizado para envio de e-mails:

Enviar e-mail texto (simples)

Enviar e-mail HTML usando templates

Padronizar comunicação com o usuário (notificações do sistema)

Manter estrutura modular:

Controller → DTO → Service → Template → SMTP

2) Tecnologias Utilizadas

Python 3.10+ — linguagem

FastAPI — API REST

Uvicorn — servidor ASGI

Pydantic — validação de DTOs

Jinja2 — renderização de templates HTML

SMTP (Gmail/Outlook/Servidor SMTP) — envio real de e-mail

3) Estrutura do Projeto
email-api-python/
│
├── app/
│   ├── controllers/
│   │     └── email_controller.py
│   ├── dtos/
│   │     └── enviar_email_dto.py
│   ├── models/
│   │     └── email_model.py
│   ├── services/
│   │     ├── email_service.py
│   │     └── smtp_service.py
│   ├── templates/
│   │     ├── email_template.html
│   │     ├── inscricao_confirmada.html
│   │     ├── cancelamento_inscricao.html
│   │     └── checkin_confirmado.html
│   └── utils/
│         └── template_utils.py
│
├── app/main.py   (ou main.py, conforme seu projeto)
└── README.md


Observação: o nome exato do arquivo de entrada pode ser main.py na raiz ou app/main.py. O importante é o comando do Uvicorn apontar para o app.

4) Funcionamento (fluxo de envio)
4.1 E-mail texto

Controller recebe o DTO

DTO valida destinatario, assunto, mensagem

Service cria EmailModel

SMTPService envia com html=False

API retorna JSON confirmando envio

4.2 E-mail HTML (template)

Controller recebe o DTO

Service escolhe o template correto (ex.: inscrição/cancelamento/check-in)

TemplateUtils.render() injeta variáveis no HTML (ex.: nome, evento, data, local)

SMTPService envia com html=True

API retorna JSON confirmando envio

5) Templates HTML suportados

Templates (Jinja2) usados para padronização:

inscricao_confirmada.html

cancelamento_inscricao.html

checkin_confirmado.html

email_template.html (genérico)

Cada template usa variáveis como:

{{ nome }}

{{ evento }}

{{ data }} (quando aplicável)

{{ local }} (quando aplicável)

{{ assunto }} / {{ mensagem }} (no template genérico)

6) Endpoints

Os nomes abaixo seguem o padrão mais comum; ajuste se no seu email_controller.py estiver diferente.

6.1 Enviar e-mail texto

POST /emails/enviar

Body:

{
  "destinatario": "usuario@email.com",
  "assunto": "Confirmação",
  "mensagem": "Sua inscrição foi confirmada."
}


Resposta (exemplo):

{
  "status": "ok",
  "tipo": "texto",
  "destinatario": "usuario@email.com"
}

6.2 Enviar e-mail HTML (template)

POST /emails/enviar-html

Body:

{
  "destinatario": "usuario@email.com",
  "assunto": "Inscrição confirmada",
  "mensagem": "Workshop de Microsserviços"
}


Resposta (exemplo):

{
  "status": "ok",
  "tipo": "html",
  "destinatario": "usuario@email.com"
}


Importante: para e-mails de inscrição/cancelamento/check-in, o ideal é o backend (Events API) enviar também os campos nome, evento, data, local (se o seu DTO suportar), ou então o Email API montar isso baseado em um “tipo de template”.
Se hoje o DTO tem só destinatario/assunto/mensagem, o HTML vai ser montado com dados genéricos (ex.: nome="Participante").

7) Integração no Sistema de Eventos

Normalmente, quem chama o Email API é a Events API, por exemplo quando:

Inscrição confirmada → envia inscricao_confirmada.html

Cancelamento de inscrição → envia cancelamento_inscricao.html

Check-in/presença registrada → envia checkin_confirmado.html

Assim, o portal não precisa disparar e-mails diretamente: ele chama a Events API, e a Events API dispara o e-mail.

8) Segurança

A API pode funcionar sem autenticação durante o MVP.

Em produção/entrega, é comum proteger com:

token interno (header fixo)

JWT (integrado com Auth API)

ou restrição por rede (somente backend acessa)

Hoje: manter simples, mas lembrar que “email API aberta” permite abuso se exposta publicamente.

9) Como executar localmente

Instalar dependências:

pip install fastapi uvicorn jinja2


Rodar:

uvicorn app.main:app --reload --port 8003


(ou uvicorn main:app --reload --port 8003 conforme seu entrypoint)

Abrir Swagger:

http://localhost:8003/docs

10) Configuração SMTP

O envio real depende de variáveis/configurações usadas no smtp_service.py, como:

Host SMTP (ex.: smtp.gmail.com)

Porta (ex.: 587)

Usuário

Senha / App Password

TLS/SSL

Recomendado: guardar em .env e ler via os.getenv().

11) Status do Microserviço

Envio SMTP real: ✅ OK

Envio em texto: ✅ OK

Envio HTML com templates (Jinja2): ✅ OK

Templates específicos (inscrição/cancelamento/check-in): ✅ OK

Swagger: ✅ OK

12) Desenvolvido por

Matheus Vargas — Email API (FastAPI + SMTP + Templates HTML)EMAIL API — Serviço de Notificações por E-mail (HTML Templates + SMTP) — Python + FastAPI

Este microserviço é responsável por enviar e-mails reais do Sistema de Eventos via SMTP, suportando envio em texto e em HTML com templates (Jinja2).
Ele é acionado principalmente pelo backend (ex.: Events API) para notificar ações como inscrição, cancelamento e check-in/presença.

1) Objetivo

Disponibilizar um serviço centralizado para envio de e-mails:

Enviar e-mail texto (simples)

Enviar e-mail HTML usando templates

Padronizar comunicação com o usuário (notificações do sistema)

Manter estrutura modular:

Controller → DTO → Service → Template → SMTP

2) Tecnologias Utilizadas

Python 3.10+ — linguagem

FastAPI — API REST

Uvicorn — servidor ASGI

Pydantic — validação de DTOs

Jinja2 — renderização de templates HTML

SMTP (Gmail/Outlook/Servidor SMTP) — envio real de e-mail

3) Estrutura do Projeto
email-api-python/
│
├── app/
│   ├── controllers/
│   │     └── email_controller.py
│   ├── dtos/
│   │     └── enviar_email_dto.py
│   ├── models/
│   │     └── email_model.py
│   ├── services/
│   │     ├── email_service.py
│   │     └── smtp_service.py
│   ├── templates/
│   │     ├── email_template.html
│   │     ├── inscricao_confirmada.html
│   │     ├── cancelamento_inscricao.html
│   │     └── checkin_confirmado.html
│   └── utils/
│         └── template_utils.py
│
├── app/main.py   (ou main.py, conforme seu projeto)
└── README.md


Observação: o nome exato do arquivo de entrada pode ser main.py na raiz ou app/main.py. O importante é o comando do Uvicorn apontar para o app.

4) Funcionamento (fluxo de envio)
4.1 E-mail texto

Controller recebe o DTO

DTO valida destinatario, assunto, mensagem

Service cria EmailModel

SMTPService envia com html=False

API retorna JSON confirmando envio

4.2 E-mail HTML (template)

Controller recebe o DTO

Service escolhe o template correto (ex.: inscrição/cancelamento/check-in)

TemplateUtils.render() injeta variáveis no HTML (ex.: nome, evento, data, local)

SMTPService envia com html=True

API retorna JSON confirmando envio

5) Templates HTML suportados

Templates (Jinja2) usados para padronização:

inscricao_confirmada.html

cancelamento_inscricao.html

checkin_confirmado.html

email_template.html (genérico)

Cada template usa variáveis como:

{{ nome }}

{{ evento }}

{{ data }} (quando aplicável)

{{ local }} (quando aplicável)

{{ assunto }} / {{ mensagem }} (no template genérico)

6) Endpoints

Os nomes abaixo seguem o padrão mais comum; ajuste se no seu email_controller.py estiver diferente.

6.1 Enviar e-mail texto

POST /emails/enviar

Body:

{
  "destinatario": "usuario@email.com",
  "assunto": "Confirmação",
  "mensagem": "Sua inscrição foi confirmada."
}


Resposta (exemplo):

{
  "status": "ok",
  "tipo": "texto",
  "destinatario": "usuario@email.com"
}

6.2 Enviar e-mail HTML (template)

POST /emails/enviar-html

Body:

{
  "destinatario": "usuario@email.com",
  "assunto": "Inscrição confirmada",
  "mensagem": "Workshop de Microsserviços"
}


Resposta (exemplo):

{
  "status": "ok",
  "tipo": "html",
  "destinatario": "usuario@email.com"
}


Importante: para e-mails de inscrição/cancelamento/check-in, o ideal é o backend (Events API) enviar também os campos nome, evento, data, local (se o seu DTO suportar), ou então o Email API montar isso baseado em um “tipo de template”.
Se hoje o DTO tem só destinatario/assunto/mensagem, o HTML vai ser montado com dados genéricos (ex.: nome="Participante").

7) Integração no Sistema de Eventos

Normalmente, quem chama o Email API é a Events API, por exemplo quando:

Inscrição confirmada → envia inscricao_confirmada.html

Cancelamento de inscrição → envia cancelamento_inscricao.html

Check-in/presença registrada → envia checkin_confirmado.html

Assim, o portal não precisa disparar e-mails diretamente: ele chama a Events API, e a Events API dispara o e-mail.

8) Segurança

A API pode funcionar sem autenticação durante o MVP.

Em produção/entrega, é comum proteger com:

token interno (header fixo)

JWT (integrado com Auth API)

ou restrição por rede (somente backend acessa)

Hoje: manter simples, mas lembrar que “email API aberta” permite abuso se exposta publicamente.

9) Como executar localmente

Instalar dependências:

pip install fastapi uvicorn jinja2


Rodar:

uvicorn app.main:app --reload --port 8003


(ou uvicorn main:app --reload --port 8003 conforme seu entrypoint)

Abrir Swagger:

http://localhost:8002/docs

10) Configuração SMTP

O envio real depende de variáveis/configurações usadas no smtp_service.py, como:

Host SMTP (ex.: smtp.gmail.com)

Porta (ex.: 587)

Usuário

Senha / App Password

TLS/SSL

Recomendado: guardar em .env e ler via os.getenv().

11) Status do Microserviço

Envio SMTP real: ✅ OK

Envio em texto: ✅ OK

Envio HTML com templates (Jinja2): ✅ OK

Templates específicos (inscrição/cancelamento/check-in): ✅ OK

Swagger: ✅ OK

12) Desenvolvido por

Matheus Vargas — Email API (FastAPI + SMTP + Templates HTML)