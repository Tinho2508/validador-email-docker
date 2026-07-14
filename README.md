# API Validadora de E-mails

API RESTful simples em **Python/Flask** para validação de formato e domínio de
endereços de e-mail, empacotada com **Docker** e com **testes automatizados**
executados via **CI/CD** (GitHub Actions).

Projeto de portfólio criado para consolidar prática com back-end, containerização
e boas práticas de engenharia de software.

## ✨ Funcionalidades

- `POST /validate` — valida o formato do e-mail (regex) e verifica se o
  domínio resolve via DNS.
- `GET /health` — health check simples, útil para orquestração em containers.

## 🧱 Stack

- Python 3.12
- Flask
- Pytest (testes automatizados)
- Docker / Docker Compose
- GitHub Actions (CI/CD)

## 🚀 Como rodar localmente (sem Docker)

```bash
pip install -r requirements.txt
python app.py
```

A API sobe em `http://localhost:5000`.

## 🐳 Como rodar com Docker

```bash
docker build -t email-validator-api .
docker run -p 5000:5000 email-validator-api
```

Ou, de forma ainda mais simples, com Docker Compose:

```bash
docker compose up --build
```

## 🧪 Rodando os testes

```bash
pip install -r requirements.txt
pytest -v
```

Os mesmos testes rodam automaticamente a cada `push`/`pull request` via
GitHub Actions (veja `.github/workflows/ci.yml`).

## 📬 Exemplo de uso

```bash
curl -X POST http://localhost:5000/validate \
  -H "Content-Type: application/json" \
  -d '{"email": "contato@gmail.com"}'
```

Resposta:

```json
{
  "email": "contato@gmail.com",
  "formato_valido": true,
  "dominio_resolvivel": true,
  "valido": true
}
```

## 📂 Estrutura do projeto

```
email-validator-api/
├── app.py                     # Aplicação Flask
├── tests/
│   └── test_app.py            # Testes automatizados (pytest)
├── Dockerfile                 # Imagem Docker da aplicação
├── docker-compose.yml         # Orquestração local
├── requirements.txt           # Dependências Python
└── .github/workflows/ci.yml   # Pipeline de CI/CD
```

## 👤 Autor

José Ailton F. da Silva — [LinkedIn](https://linkedin.com/in/jose-ailton-fda-silva) · [GitHub](https://github.com/Tinho2508)
# validador-email-docker
