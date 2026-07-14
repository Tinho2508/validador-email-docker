"""
API Validadora de E-mails
--------------------------
API RESTful simples em Flask para validação de formato e domínio de
endereços de e-mail. Projeto de portfólio para demonstrar Python,
Flask, testes automatizados e containerização com Docker.
"""

import re
import socket
from flask import Flask, request, jsonify

app = Flask(__name__)

# Regex básica para validação de formato (RFC 5322 simplificado)
EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def is_valid_format(email: str) -> bool:
    """Verifica se o e-mail tem um formato sintaticamente válido."""
    if not email or "@" not in email:
        return False
    return bool(EMAIL_REGEX.match(email))


def has_valid_domain(email: str) -> bool:
    """
    Verifica se o domínio do e-mail resolve via DNS (MX/A record básico).
    Retorna False silenciosamente se não houver rede disponível.
    """
    try:
        domain = email.split("@")[1]
        socket.gethostbyname(domain)
        return True
    except (IndexError, socket.gaierror, socket.error):
        return False


@app.route("/health", methods=["GET"])
def health():
    """Endpoint simples de health check (útil para orquestração/Docker)."""
    return jsonify({"status": "ok"}), 200


@app.route("/validate", methods=["POST"])
def validate_email():
    """
    Recebe um JSON {"email": "..."} e retorna a validação de formato
    e, opcionalmente, se o domínio resolve na rede.
    """
    data = request.get_json(silent=True) or {}
    email = data.get("email", "").strip()

    if not email:
        return jsonify({"error": "Campo 'email' é obrigatório."}), 400

    format_ok = is_valid_format(email)
    domain_ok = has_valid_domain(email) if format_ok else False

    return jsonify({
        "email": email,
        "formato_valido": format_ok,
        "dominio_resolvivel": domain_ok,
        "valido": format_ok and domain_ok,
    }), 200


if __name__ == "__main__":
    # host 0.0.0.0 é necessário para expor a API fora do container Docker
    app.run(host="0.0.0.0", port=5000, debug=False)
