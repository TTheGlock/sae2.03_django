from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form):

    TYPE2 = (
        ('PC', ('PC − Run windows')),
        ('Mac', ('Mac − Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch − To maintains and connect servers')),
    )

    #nom de la machine
    nom = forms.CharField(required=True, label='Nom de la machine')
    #type de la machine
    mach = forms.ChoiceField(choices=TYPE2) 
    
    def clean_nom(self):
        data_m=self.cleaned_data["nom"]
        if len(data_m) > 60:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data_m
    
    def clean_mach(self):
        data_m=self.cleaned_data["mach"]
        if len(data_m) > 32:
            raise ValidationError(("Erreur de format pour le champ mach"))
        return data_m
    
class AddPersonnelForm(forms.Form):

    nom = forms.CharField(required=True, label='Nom de la personne')
    prenom = forms.CharField(required=True, label='Prénom de la personne')
    id = forms.IntegerField(required=True, label='ID de la personne')
    
    def clean_nom(self):
        data_p=self.cleaned_data["nom"]
        if len(data_p) > 60:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data_p

    def clean_prenom(self):
        data_p=self.cleaned_data["prenom"]
        if len(data_p) > 60:
            raise ValidationError(("Erreur de format pour le champ prenom"))
        return data_p

    def clean_id(self):
        data_p=self.cleaned_data["id"]
        if data_p < 1000000000000 and data_p > 2999999999999:
            raise ValidationError(("Erreur de format pour le champ id"))
        return data_p