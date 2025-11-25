EMAIL API — Serviço de Envio Básico de E-mails (Python + FastAPI)

Este microserviço é responsável por enviar e-mails simples utilizando parâmetros enviados via API.
Faz parte da arquitetura de microserviços do Sistema de Eventos.

1. Objetivo

Permitir o envio básico de e-mails:

Receber dados via DTO

Criar um objeto EmailModel

Retornar resposta JSON após processamento

Estrutura modular (Controller → DTO → Service → Model)

A parte avançada (HTML template, SMTP real, autenticação) será implementada posteriormente.

2. Tecnologias Utilizadas
Tecnologia	Finalidade
Python 3.10+	Linguagem
FastAPI	Backend REST
Pydantic	Validação de DTOs
Uvicorn	Servidor ASGI
Jinja2 (posterior)	Templates HTML
SMTP real (posterior)	Envio real de e-mails

Importante: nesta fase inicial não há envio real de e-mails.

3. Estrutura do Projeto
EMAIL-API-PYTHON/
│
├── app/
│   ├── controllers/
│   │     └── email_controller.py
│   ├── dtos/
│   │     └── enviar_email_dto.py
│   ├── models/
│   │     └── email_model.py
│   ├── services/
│   │     └── email_service.py
│   ├── templates/          (não utilizado nesta fase)
│   └── utils/              (não utilizado nesta fase)
│
├── main.py
└── README.md

4. Fluxo de Envio de E-mail (fase atual)

Controller recebe o DTO

DTO valida os campos obrigatórios

Serviço processa os dados

Retorna resposta JSON para o cliente

Nesta etapa não há integração SMTP nem HTML template.

5. Endpoints
5.1 Enviar e-mail simples

POST /emails/enviar

Request:

{
  "destinatario": "usuario@email.com",
  "assunto": "Confirmação",
  "mensagem": "Inscrição realizada com sucesso."
}


Response:

{
  "destinatario": "usuario@email.com",
  "assunto": "Confirmação",
  "mensagem": "Inscrição realizada com sucesso.",
  "status": "Email processado"
}


Retorno pode ser ajustado na fase avançada conforme integrações.

6. Componentes Implementados
Controller — email_controller.py

Recebe DTO

Chama serviço

Retorna JSON

DTO — enviar_email_dto.py

Validação via Pydantic

Campos obrigatórios:

destinatario

assunto

mensagem

Model — email_model.py

Representação simples do e-mail

Armazena informações básicas

Service — email_service.py

Constrói EmailModel

Simula envio (sem SMTP)

Retorna JSON

7. Segurança (fase atual)

API sem autenticação

Não usa JWT

Não integra com Auth API

Sem perfis

Segurança será aplicada posteriormente pelo time (padrão microserviços).

8. Executando Localmente

Instalar dependências mínimas:

pip install fastapi uvicorn


Rodar API:

uvicorn main:app --reload --port 8002

9. Testes via Postman

1️⃣ Enviar e-mail

POST http://127.0.0.1:8002/emails/enviar


Body JSON:

{
  "destinatario": "user@mail.com",
  "assunto": "Bem-vindo",
  "mensagem": "Seu registro foi confirmado."
}

10. Documentação Swagger

Swagger UI:

http://localhost:8002/docs


Redoc:

http://localhost:8002/redoc

11. Status do Microserviço
Feature	Status
DTO básico	✔️
Controller básico	✔️
Model simples	✔️
Service simples	✔️
Envio HTML	🔜 EZ
Template	🔜 EZ
SMTP real	🔜 MT
Integração Auth/Events	🔜 posterior
Segurança	🔜 posterior
12. Próximas Etapas (EZ)

Implementar template HTML via Jinja2

Criar serviço de email em HTML

Ajustar respostas do controller

Estrutura para Streaming / anexo

13. Desenvolvido por

Matheus Vargas — Email API (MVP)