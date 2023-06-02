# sae2.03_django
Sae 2.03, création d'un site web à partir de Django

## Installation

- `git clone git@github.com:TTheGlock/sae2.03_django.git` (me demander le mot de passe)
- ou téléchargement du fichier en .zip

## Démarrage

- `source virtualenv/djangoenv/bin/activate`
- `python3 computermngt/manage.py makemigrations`
- `python3 computermngt/manage.py migrate`
- `python3 computermngt/manage.py runserver`

## Informations additionnelles 

### ⚠️ Pour des raisons de sécurité, les bases de données ne sont pas envoyées sur le dépôt Github ⚠️
Il faudra donc recréer les identifiants administrateur à chaque récupération :

1. Vérification :
- se placer dans `/computermngt`
- `python3 manage.py shell`
- `from django.contrib.auth import get_user_model`
- `list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))`

2. Création : 
- `python manage.py createsuperuser`
- suivre les directives et rentrer l'identifiant `admin` et le mot de passe `gtrnet`
