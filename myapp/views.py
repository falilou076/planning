from django.shortcuts import render, reverse, redirect
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
##########################
##########################
def login_user(request):
    error=False

    if request.method =="POST":
        form=ConnexionForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            #Verification des donnees
            user=authenticate(username=username, password=password)
            if user: #L'objet renvoye n'est pas Null
                login(request,user) #Collecte de l'utilisateur
                respons_ped=Responsable_Prof.objects.filter(user=user)
                prof=Prof.objects.filter(user=user)
                if respons_ped:
                    return render(request,'blog/index.html',{'respons_ped':respons_ped})
                elif prof:
                    return render(request,'blog/prof.html',{'prof':prof})

                else:
                    return render(request,'blog/test.html',locals())

                
            else: #Une erreur s'affiche
                error=True

    else:
        form=ConnexionForm()
        #return redirect(reverse('connexion'))
    return render(request,'blog/login.html',locals())
##########################
##########################

def home_prof(request):
    return render(request,'blog/prof.html',locals())



####Deconnexion
@login_required(login_url='login')
def deconnexion(request):
    logout(request)
    return redirect(reverse('login'))#using the the name url




@login_required(login_url='login')
def Index(request):
    planning  = Planning.objects.all()
    return render(request, 'blog/index.html', locals())

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def delPlanning(request, id):
    planning = Planning.objects.get(id=id)
    planning.delete()
    return redirect(reverse("index"))


@login_required(login_url='login')
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

@login_required(login_url='login')
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


@login_required(login_url='login')
def liste(request):
    eleves  = Eleve.objects.all()
    return render(request, 'blog/liste.html', locals())

###View pour prof
@login_required(login_url='login')
def liste_eleve_prof(request):
    eleves  = Eleve.objects.all()
    return render(request, 'blog/prof/liste_eleves.html', locals())

@login_required(login_url='login')
def liste_eleve(request):
    eleves  = Eleve.objects.all()
    profs = Prof.objects.all()
    return render(request, 'blog/liste_eleve.html', locals())


@login_required(login_url='login')
def delEleve(request,id):
    eleves = Eleve.objects.get(id=id)
    eleves.delete()
    return redirect(reverse("liste"))

@login_required(login_url='login')
def notifications(request):
    notif = Notification.objects.filter(id_prof_recep=1)
    notif1 = Notification.objects.filter(id_prof_emmet=1)
    res = Prof.objects.all()
    form = NotificationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            contenu = form.cleaned_data['contenu']
            id_prof_emmet = form.cleaned_data['id_prof_emmet']
            id_prof_recep = form.cleaned_data['id_prof_recep']
            form.save()
            return redirect(reverse("index"))
    return render(request, 'blog/notification.html', locals())

@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def Index_eleve(request):
    planning  = Planning.objects.all()
    return render(request, 'blog/index_eleve.html', locals())


@login_required(login_url='login')
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


##############Plaquette prof##########################
#####################################################
@login_required(login_url='login')
def IndexPlaquetteProf(request):
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
    return render(request, 'blog/prof/plaquette_prof.html', locals())


@login_required(login_url='login')
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
################ end plaquette prof#########################



@login_required(login_url='login')
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


@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def DelPlaquette(request, id):
    plaquettes = Plaquette.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))

@login_required(login_url='login')
def DelPlaquette1(request, id):
    plaquettes = Plaquette1.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))


@login_required(login_url='login')
def DelPlaquette2(request, id):
    plaquettes = Plaquette2.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))

@login_required(login_url='login')
def DelPlaquette3(request, id):
    plaquettes = Plaquette3.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))

@login_required(login_url='login')
def DelPlaquette4(request, id):
    plaquettes = Plaquette4.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("plaquette"))

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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