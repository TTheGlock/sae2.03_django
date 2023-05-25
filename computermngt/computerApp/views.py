from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .forms import AddMachineForm
from .forms import AddPersonnelForm

from computerApp.models import Machine
from computerApp.models import Personnel

def index(request):
    # Ajout de la ligne de recuperation des machine
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    # Que l’on passe en parametre de la page html via la syntaxe suivante
    context = {}
    return render(request, 'index.html', context)

#liste des machines
def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines':machines}
    return render(request,'computerApp/machine_list.html',context)

#liste du personnel
def personnel_list_view(request) :
    personnels = Personnel.objects.all()
    context={'personnels':personnels}
    return render(request,'computerApp/personnel_list.html',context)

#details des machines
def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine' : machine}
    return render(request, 'computerApp/machine_detail.html', context)

#details des personnes
def personnel_detail_view(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    context = {'personnel' : personnel}
    return render(request, 'computerApp/personnel_detail.html', context)

#création de machines
def machine_add_form(request):
    if request.method == 'POST' :
        form = AddMachineForm(request.POST or None)
        if form .is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'],
                                  mach=form.cleaned_data['mach'])
            new_machine.save()
            return redirect('machines')  
    else :
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/add_machine.html', context)

#création de personnel
def personnel_add_form(request):
    if request.method == 'POST' :
        form = AddPersonnelForm(request.POST or None)
        if form .is_valid():
            new_personnel = Personnel(nom=form.cleaned_data['nom'],
                                      prenom=form.cleaned_data['prenom'], 
                                      id=form.cleaned_data['id'])
            new_personnel.save()
            return redirect('personnels')  
    else :
        form = AddPersonnelForm()
        context = {'form': form}
        return render(request, 'computerApp/add_personnel.html', context)
