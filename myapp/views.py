from django.shortcuts import render, reverse, redirect
from .forms import EleveForm, PlanningForm
from .models import Eleve, Planning
# Create your views here.

def addPlanning(request):
    form = PlanningForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            heure = form.cleaned_data['heure']
            moduleLundi = form.cleaned_data['moduleLundi']
            moduleMardi = form.cleaned_data['moduleMardi']
            moduleMercredi = form.cleaned_data['moduleMercredi']
            moduleJeudi = form.cleaned_data['moduleJeudi']
            moduleVendredi = form.cleaned_data['moduleVendredi']
            moduleSamedi = form.cleaned_data['moduleSamedi']
            form.save()
            return redirect(reverse("index"))
    return render(request, 'blog/add.html', locals())

def editPlanning(request,id):
    planning = Planning.objects.get(id=id)
    form = PlanningForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            planning.heure = form.cleaned_data['heure']
            planning.moduleLundi = form.cleaned_data['moduleLundi']
            planning.moduleMardi = form.cleaned_data['moduleMardi']
            planning.moduleMercredi = form.cleaned_data['moduleMercredi']
            planning.moduleJeudi = form.cleaned_data['moduleJeudi']
            planning.moduleVendredi = form.cleaned_data['moduleVendredi']
            planning.moduleSamedi = form.cleaned_data['moduleSamedi']
            planning.save()
            return redirect(reverse("index"))
    return render(request, 'blog/edit.html', locals())


def delPlanning(request, id):
    planning = Planning.objects.get(id=id)
    planning.delete()
    return redirect(reverse("index"))
    return render(request, 'blog/del.html', locals())


def ajout(request):
    grade  = 0
    eleves = Eleve.objects.all()
    for eleve in eleves:
        if eleve.typeEleve == 'Responsable de classe':
            grade = 1
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            classe = form.cleaned_data['classe']
            typeEleve = form.cleaned_data['typeEleve']
            form.save()
            return redirect(reverse("ajout"))
    return render(request, 'blog/ajout.html', locals())

def editEleve(request,id):
    grade  = 0
    eleves = Eleve.objects.all()
    for eleve in eleves:
        if eleve.typeEleve == 'Responsable de classe':
            grade = 1
    eleve = Eleve.objects.get(id=id)
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            eleve.prenom = form.cleaned_data['prenom']
            eleve.nom = form.cleaned_data['nom']
            eleve.classe = form.cleaned_data['classe']
            eleve.typeEleve = form.cleaned_data['typeEleve']
            eleve.save()
            return redirect(reverse("liste"))
    return render(request, 'blog/editEleve.html', locals())



def liste(request):
    eleves  = Eleve.objects.all()
    return render(request, 'blog/liste.html', locals())


def delEleve(request,id):
    eleves = Eleve.objects.get(id=id)
    eleves.delete()
    return redirect(reverse("liste"))


def reception(request):
    return render(request, 'blog/reception.html', locals())

def envoi(request):
        return render(request, 'blog/envoi.html', locals())