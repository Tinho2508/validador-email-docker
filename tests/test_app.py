"""
Testes automatizados da API Validadora de E-mails.
Executar com: pytest -v
"""

import pytest
from app import app, is_valid_format


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# --- Testes unitários da função de validação de formato ---

def test_formato_valido():
    assert is_valid_format("usuario@exemplo.com") is True


def test_formato_invalido_sem_arroba():
    assert is_valid_format("usuarioexemplo.com") is False


def test_formato_invalido_sem_dominio():
    assert is_valid_format("usuario@") is False


def test_formato_invalido_vazio():
    assert is_valid_format("") is False


# --- Testes de integração dos endpoints da API ---

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_validate_sem_email(client):
    response = client.post("/validate", json={})
    assert response.status_code == 400


def test_validate_formato_invalido(client):
    response = client.post("/validate", json={"email": "invalido"})
    assert response.status_code == 200
    body = response.get_json()
    assert body["formato_valido"] is False
    assert body["valido"] is False


def test_validate_formato_valido_dominio_conhecido(client):
    response = client.post("/validate", json={"email": "contato@gmail.com"})
    assert response.status_code == 200
    body = response.get_json()
    assert body["formato_valido"] is True
