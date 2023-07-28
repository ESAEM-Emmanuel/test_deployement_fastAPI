# Utilisation de l'image de base officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE some tcp/udp ports
EXPOSE 8000

# Copier l'ensemble de l'application dans le conteneur
COPY . .

# Définir la commande par défaut pour exécuter l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400"]