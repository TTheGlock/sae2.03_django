from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator

#classe "Machines"

class Machine(models.Model):

    TYPE = (
        ('PC', ('PC − Run windows')),
        ('Mac', ('Mac − Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch − To maintains and connect servers')),
    )
    #id de la machine
    id = models.AutoField(primary_key=True, editable=False)
    #nom de la machine
    nom = models.CharField(max_length=6)
    #dernière date de maintenance
    maintenanceDate = models.DateField(default=datetime.now())
    #type de la machine
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

#classe "Personnel"

class Personnel(models.Model):
    #num de securité social, max 13 int, modifiable
    id = models.PositiveIntegerField(primary_key=True, editable=True, validators=[MaxValueValidator(9999999999999)])
    #nom, max 200 char
    nom = models.CharField(max_length=200)
    #nom, max 200 char
    prenom = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + " -> " + self.nom + " " + self.prenom