FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie de l'application
COPY app/ /app/app/
COPY docker/ /app/docker/

# Exposition du port
EXPOSE 8501

# Commande de démarrage
CMD ["streamlit", "run", "/app/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"] 