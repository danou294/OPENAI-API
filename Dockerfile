# Utilisez une image Python officielle en tant que base
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt requirements.txt

# Installez les autres dépendances du projet
RUN pip install -r requirements.txt

# Copiez tout le contenu du répertoire actuel dans le répertoire de travail du conteneur
COPY . .

# Exposez le port 8000 pour que l'application soit accessible depuis l'extérieur du conteneur
EXPOSE 8000

# Commande pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
