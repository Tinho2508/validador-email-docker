# Imagem base leve com Python 3.12
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o requirements primeiro (aproveita cache de camadas do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY app.py .
COPY tests/ tests/

# Porta exposta pela API Flask
EXPOSE 5000

# Variável de ambiente para garantir logs sem buffer no container
ENV PYTHONUNBUFFERED=1

# Comando padrão ao iniciar o container
CMD ["python", "app.py"]
