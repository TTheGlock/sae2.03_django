# sae2.03_django
Sae 2.03, création d'un site web à partir de Django

## Installation

- `git clone git@github.com:TTheGlock/sae2.03_django.git`
- ou téléchargement du fichier en .zip

## Démarrage

- `source virtualenv/djangoenv/bin/activate`
- `python3 computermngt/manage.py makemigrations`
- `python3 computermngt/manage.py migrate`
- `python3 computermngt/manage.py runserver`

## Informations additionnelles 

Connexion admin :
- username : admin
- password : gtrnet

## Possibles problèmes

### 1. Identifiants incorrects

dans `/computermngt` :
- `python3 manage.py shell`
- `from django.contrib.auth import get_user_model`
- `list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))`

si cette commande ne renvoie rien, alors les identiants sont incorrects car ils n'existent pas.

il va donc falloir les créer :
- `python manage.py createsuperuser`
- suivre les directives et rentrer les identifiants précédents
