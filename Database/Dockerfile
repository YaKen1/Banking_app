# Utiliser l'image de base MySQL
FROM mysql:8.0

# Copier le fichier SQL d'initialisation de la base de donnée
COPY bank.sql /docker-entrypoint-initdb.d/

# Définir le varibale d'environment pour l'utilisateur
ENV MYSQL_ROOT_USER=root

# Définir le mot de passe de l'utilisateur
ENV MYSQL_ROOT_PASSWORD=kali

# Dèfinir la base de donnée
ENV MYSQL_DATABASE=bank

# Exposer le port du MySQL (3306 par défaut)
EXPOSE 3306

