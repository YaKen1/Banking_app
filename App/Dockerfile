# Utiliser python:3.7 comme image de base de notre image
FROM python:3.7-slim

# Définir le répertoire de travail (Working directory)  dans le conteneur.
WORKDIR /app

# Installer les dépendences pour mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev gcc musl-dev && \
    rm -rf /var/lib/apt/lists/* 

# Copier le fichier "requirements" dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendences
RUN pip install --no-cache-dir -r requirements.txt

# Copier du source code de l'application dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application Flask s'exécutera
EXPOSE 5000

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=main.py

# Exécuter l'application Flask lorsque le conteneur démarre
CMD ["flask", "run", "--host=0.0.0.0"]
