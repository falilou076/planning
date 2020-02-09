from django.shortcuts import render, reverse, redirect
from .forms import *
from .models import *
# Create your views here.

def Index(request):
    planning  = Planning.objects.all()
    return render(request, 'blog/index.html', locals())

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
            id_prof = form.cleaned_data['id_prof']
            id_classe = form.cleaned_data['id_classe']
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
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prenom_eleve = form.cleaned_data['prenom']
            nom_eleve = form.cleaned_data['nom']
            id_classe = form.cleaned_data['classe']
            form.save()
            return redirect(reverse("ajout"))
    return render(request, 'blog/ajout.html', locals())

def editEleve(request,id):
    eleve = Eleve.objects.get(id=id)
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            eleve.prenom_eleve= form.cleaned_data['prenom']
            eleve.nom_eleve = form.cleaned_data['nom']
            eleve.id_classe = form.cleaned_data['classe']
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


def notifications(request):
    form = NotificationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            contenu = form.cleaned_data['contenu']
            id_prof = form.cleaned_data['id_prof']
            form.save()
            return redirect(reverse("ajout"))
    return render(request, 'blog/ajout.html', locals())

def cahier_texte(request):
    form = NotificationForm(request.POST or None)
    cours = Cours.objects.all()
    if request.method == "POST":
        if form.is_valid():
            heure_cours = form.cleaned_data['heure_cours']
            date = form.cleaned_data['date']
            contenu = form.cleaned_data['contenu']
            id_eleve = form.cleaned_data['id_eleve']
            id_cours = form.cleaned_data['id_cours']
            form.save()
            return redirect(reverse("ajout"))
    return render(request, 'blog/cahierTexte.html', locals())

def lirecahierTexte(request):
    cahiertexte  = cahier_texte.objects.all()
    return render(request, 'blog/lire_cahier_texte.html', locals())

def presence_absence(request):
    eleves = Eleve.objects.all()
    cours = Cours.objects.all()
    form = PresAbsenceForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            id_eleve = form.cleaned_data['id_eleve']
            id_cours = form.cleaned_data['id_cours']
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            form.save()
            return redirect(reverse("ajout"))
    return render(request, 'blog/presence_absence.html', locals())


def lirepresence(request):
    presenceAbsence  = presence_absence.objects.all()
    return render(request, 'blog/liste.html', locals())