from django.shortcuts import render, reverse, redirect
from .forms import *
from .models import *
# Create your views here.

def Index(request):
    planning  = Planning.objects.all()
    return render(request, 'blog/index.html', locals())

def addPlanning(request):
    form = PlanningForm(request.POST or None)
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    classe = Classe.objects.all()
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
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    classe = Classe.objects.all()
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
    classe = Classe.objects.all()
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prenom_eleve = form.cleaned_data['prenom_eleve']
            nom_eleve = form.cleaned_data['nom_eleve']
            id_classe = form.cleaned_data['id_classe']
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

def liste_eleve(request):
    eleves  = Eleve.objects.all()
    profs = Prof.objects.all()
    return render(request, 'blog/liste_eleve.html', locals())


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
    cours = Cours.objects.all()
    eleves = Responsable_Eleve.objects.all()
    cahiertexte = CahierTexte.objects.all()
    form = CahierTexteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            heure_cours = form.cleaned_data['heure_cours']
            date = form.cleaned_data['date']
            contenu = form.cleaned_data['contenu']
            id_eleve = form.cleaned_data['id_eleve']
            id_cours = form.cleaned_data['id_cours']
            form.save()
            return redirect(reverse("cahierTexte"))
    return render(request, 'blog/cahierTexte.html', locals())



def presence_absence(request):
    eleves = Eleve.objects.all()
    cours = Cours.objects.all()
    presabs = PresAbs.objects.all()
    for j in presabs:
        j.nom_eleve = str(j.nom_eleve).replace("['", "").replace("'", "").replace("]", "")
    form = PresAbsenceForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            nom_eleve = request.POST.getlist('nom_eleve')
            id_cours = form.cleaned_data['id_cours']
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            form.save()
            return redirect(reverse("presabs"))
    return render(request, 'blog/presence_absence.html', locals())


def Index_eleve(request):
    planning  = Planning.objects.all()
    return render(request, 'blog/index_eleve.html', locals())



def IndexPlaquette(request):
    ip = 0
    iw = 0
    ic = 0
    ik = 0
    im = 0
    d = 0
    e = 0
    f = 0
    g = 0
    plaquettes = Plaquette.objects.all()
    for plaquette in plaquettes:
        ip = ip + 1
        for j in plaquettes:
            if j.ec != "":
                d = 1
    plaquettes1 = Plaquette1.objects.all()
    for plaquette1 in plaquettes1:
        iw = iw + 1
        for j in plaquettes1:
            if j.ec != "":
                e = 1
    plaquettes2 = Plaquette2.objects.all()
    for plaquette2 in plaquettes2:
        ic = ic + 1
        for j in plaquettes2:
            if j.ec != "":
                f = 1
    plaquettes3 = Plaquette3.objects.all()
    for plaquette3 in plaquettes3:
        ik = ik + 1
        for j in plaquettes3:
            if j.ec != "":
                g = 1
    plaquettes4 = Plaquette4.objects.all()
    for plaquette4 in plaquettes4:
            im = im + 1
    return render(request, 'blog/plaquette.html', locals())


def AjoutPlaquette(request):
    a = 0
    c = 0
    pal = Plaquette.objects.all()
    for i in pal:
        c += 1
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ue = form.cleaned_data['ue']
            ec = form.cleaned_data['ec']
            cm = form.cleaned_data['cm']
            tpd = form.cleaned_data['tpd']
            ttal = form.cleaned_data['ttal']
            tpe = form.cleaned_data['tpe']
            ects = form.cleaned_data['ects']
            if c <= 1:
                total_Ects = form.cleaned_data['total_Ects']
                coefs = form.cleaned_data['coefs']
            coefs_details = form.cleaned_data['coefs_details']
            form.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/addPlaquette.html', locals())

def AjoutPlaquette1(request):
    a = 1
    c = 0
    pal = Plaquette1.objects.all()
    for i in pal:
        c += 1
    form = Plaquette1Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ue = form.cleaned_data['ue']
            ec = form.cleaned_data['ec']
            cm = form.cleaned_data['cm']
            tpd = form.cleaned_data['tpd']
            ttal = form.cleaned_data['ttal']
            tpe = form.cleaned_data['tpe']
            ects = form.cleaned_data['ects']
            if c <= 1:
                total_Ects = form.cleaned_data['total_Ects']
                coefs = form.cleaned_data['coefs']
            coefs_details = form.cleaned_data['coefs_details']
            form.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/addPlaquette.html', locals())

def AjoutPlaquette2(request):
    a = 2
    c = 0
    pal = Plaquette2.objects.all()
    for i in pal:
        c += 1
    form = Plaquette2Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ue = form.cleaned_data['ue']
            ec = form.cleaned_data['ec']
            cm = form.cleaned_data['cm']
            tpd = form.cleaned_data['tpd']
            ttal = form.cleaned_data['ttal']
            tpe = form.cleaned_data['tpe']
            ects = form.cleaned_data['ects']
            if c <= 1:
                total_Ects = form.cleaned_data['total_Ects']
                coefs = form.cleaned_data['coefs']
            coefs_details = form.cleaned_data['coefs_details']
            form.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/addPlaquette.html', locals())

def AjoutPlaquette3(request):
    a = 3
    c = 0
    pal = Plaquette3.objects.all()
    for i in pal:
        c += 1
    form = Plaquette3Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ue = form.cleaned_data['ue']
            ec = form.cleaned_data['ec']
            cm = form.cleaned_data['cm']
            tpd = form.cleaned_data['tpd']
            ttal = form.cleaned_data['ttal']
            tpe = form.cleaned_data['tpe']
            ects = form.cleaned_data['ects']
            if c <= 1:
                total_Ects = form.cleaned_data['total_Ects']
                coefs = form.cleaned_data['coefs']
            coefs_details = form.cleaned_data['coefs_details']
            form.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/addPlaquette.html', locals())

def AjoutPlaquette4(request):
    a = 4
    c = 0
    pal = Plaquette4.objects.all()
    for i in pal:
        c += 1
    form = Plaquette4Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ue = form.cleaned_data['ue']
            ec = form.cleaned_data['ec']
            cm = form.cleaned_data['cm']
            tpd = form.cleaned_data['tpd']
            ttal = form.cleaned_data['ttal']
            tpe = form.cleaned_data['tpe']
            ects = form.cleaned_data['ects']
            if c <= 1:
                total_Ects = form.cleaned_data['total_Ects']
                coefs = form.cleaned_data['coefs']
            coefs_details = form.cleaned_data['coefs_details']
            form.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/addPlaquette.html', locals())


def DelPlaquette(request, id):
    plaquettes = Plaquette.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))


def DelPlaquette1(request, id):
    plaquettes = Plaquette1.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))


def DelPlaquette2(request, id):
    plaquettes = Plaquette2.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))


def DelPlaquette3(request, id):
    plaquettes = Plaquette3.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))


def DelPlaquette4(request, id):
    plaquettes = Plaquette4.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))

def editPlaquette(request, id):
    a = 0
    c = 0
    pal = Plaquette.objects.all()
    for i in pal:
        c += 1
    pl = Plaquette.objects.get(id=id)
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pl.ec = form.cleaned_data['ec']
            pl.cm = form.cleaned_data['cm']
            pl.tpd = form.cleaned_data['tpd']
            pl.ttal = form.cleaned_data['ttal']
            pl.tpe = form.cleaned_data['tpe']
            pl.ects = form.cleaned_data['ects']
            pl.total_Ects = form.cleaned_data['total_Ects']
            pl.coefs = form.cleaned_data['coefs']
            pl.coefs_details = form.cleaned_data['coefs_details']
            pl.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/editPlaqutte.html', locals())

def editPlaquette1(request, id):
    a = 1
    c = 0
    pal = Plaquette1.objects.all()
    for i in pal:
        c += 1
    pl = Plaquette1.objects.get(id=id)
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pl.ec = form.cleaned_data['ec']
            pl.cm = form.cleaned_data['cm']
            pl.tpd = form.cleaned_data['tpd']
            pl.ttal = form.cleaned_data['ttal']
            pl.tpe = form.cleaned_data['tpe']
            pl.ects = form.cleaned_data['ects']
            pl.total_Ects = form.cleaned_data['total_Ects']
            pl.coefs = form.cleaned_data['coefs']
            pl.coefs_details = form.cleaned_data['coefs_details']
            pl.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/editPlaqutte.html', locals())

def editPlaquette2(request, id):
    a = 2
    c = 0
    pal = Plaquette2.objects.all()
    for i in pal:
        c += 1
    pl = Plaquette2.objects.get(id=id)
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pl.ec = form.cleaned_data['ec']
            pl.cm = form.cleaned_data['cm']
            pl.tpd = form.cleaned_data['tpd']
            pl.ttal = form.cleaned_data['ttal']
            pl.tpe = form.cleaned_data['tpe']
            pl.ects = form.cleaned_data['ects']
            pl.total_Ects = form.cleaned_data['total_Ects']
            pl.coefs = form.cleaned_data['coefs']
            pl.coefs_details = form.cleaned_data['coefs_details']
            pl.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/editPlaqutte.html', locals())

def editPlaquette3(request, id):
    a = 3
    c = 0
    pal = Plaquette3.objects.all()
    for i in pal:
        c += 1
    pl = Plaquette3.objects.get(id=id)
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pl.ec = form.cleaned_data['ec']
            pl.cm = form.cleaned_data['cm']
            pl.tpd = form.cleaned_data['tpd']
            pl.ttal = form.cleaned_data['ttal']
            pl.tpe = form.cleaned_data['tpe']
            pl.ects = form.cleaned_data['ects']
            pl.total_Ects = form.cleaned_data['total_Ects']
            pl.coefs = form.cleaned_data['coefs']
            pl.coefs_details = form.cleaned_data['coefs_details']
            pl.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/editPlaqutte.html', locals())

def editPlaquette4(request, id):
    a = 4
    c = 0
    pal = Plaquette4.objects.all()
    for i in pal:
        c += 1
    pl = Plaquette4.objects.get(id=id)
    form = PlaquetteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pl.ec = form.cleaned_data['ec']
            pl.cm = form.cleaned_data['cm']
            pl.tpd = form.cleaned_data['tpd']
            pl.ttal = form.cleaned_data['ttal']
            pl.tpe = form.cleaned_data['tpe']
            pl.ects = form.cleaned_data['ects']
            pl.total_Ects = form.cleaned_data['total_Ects']
            pl.coefs = form.cleaned_data['coefs']
            pl.coefs_details = form.cleaned_data['coefs_details']
            pl.save()
            return redirect(reverse("plaquette"), locals())
    return render(request, 'blog/editPlaqutte.html', locals())