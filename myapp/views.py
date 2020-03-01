from django.shortcuts import render, reverse, redirect
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

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
                respons_ele = Responsable_Eleve.objects.filter(user=user)
                classe = Classe.objects.filter(user=user)
                prof=Prof.objects.filter(user=user)
                secretaire=Secretaire.objects.filter(user=user)
                if respons_ped:
                    return redirect("index")
                elif prof:

                    return render(request,'blog/prof.html',{'prof':prof})
                elif respons_ele:
                    return redirect("index_eleve")
                elif classe:
                    return redirect("classe")

                    return render(request,'prof.html',{'prof':prof})
                elif secretaire:
                    return render(request,'secretaire.html',{'secretaire':secretaire})

                else:
                    return render(request,'blog/test.html',locals())

                
            else: #Une erreur s'affiche
                error=True

    else:
        form=ConnexionForm()
        #return redirect(reverse('connexion'))
    return render(request,'blog/login.html',locals())

##########################

def home_prof(request):
    return render(request,'prof.html',locals())

def home_secretaire(request):
    return render(request,'secretaire.html',locals())



####Deconnexion
@login_required(login_url='login')
def deconnexion(request):
    logout(request)
    return redirect(reverse('login'))#using the the name url




@login_required(login_url='login')
def Index(request):
    prof = Prof.objects.all()
    z = get_user(request).get_username()
    ip = 0
    iw = 0
    ic = 0
    ik = 0
    im = 0
    d = 0
    e = 0
    f = 0
    g = 0
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    classe = Classe.objects.all()
    res_profs = Responsable_Prof.objects.all()

    if (z == "Ahmed"):
        plaquettes = Plaquette.objects.filter(id_classe=1)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=1)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=1)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=1)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=1)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=1)
        plaquettes = Plaquette.objects.filter(id_classe=1)
        plaquettes1 = Plaquette1.objects.filter(id_classe=1)
        plaquettes2 = Plaquette2.objects.filter(id_classe=1)
        plaquettes3 = Plaquette3.objects.filter(id_classe=1)
        plaquettes4 = Plaquette4.objects.filter(id_classe=1)
        eleves = Eleve.objects.filter(id_classe=1)

    elif (z == "Abdoulaye"):
        plaquettes = Plaquette.objects.filter(id_classe=2)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=2)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=2)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=2)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=2)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=2)
        plaquettes = Plaquette.objects.filter(id_classe=2)
        plaquettes1 = Plaquette1.objects.filter(id_classe=2)
        plaquettes2 = Plaquette2.objects.filter(id_classe=2)
        plaquettes3 = Plaquette3.objects.filter(id_classe=2)
        plaquettes4 = Plaquette4.objects.filter(id_classe=2)
        eleves = Eleve.objects.filter(id_classe=2)
    else:
        plaquettes = Plaquette.objects.filter(id_classe=3)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=3)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=3)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=3)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=3)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=3)
        plaquettes = Plaquette.objects.filter(id_classe=3)
        plaquettes1 = Plaquette1.objects.filter(id_classe=3)
        plaquettes2 = Plaquette2.objects.filter(id_classe=3)
        plaquettes3 = Plaquette3.objects.filter(id_classe=3)
        plaquettes4 = Plaquette4.objects.filter(id_classe=3)
        eleves = Eleve.objects.filter(id_classe=3)
    return render(request, 'index.html', locals())

@login_required(login_url='login')
def addPlanning(request):
    form = PlanningForm(request.POST or None)
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        cours = Cours.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        cours = Cours.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        cours = Cours.objects.filter(id_classe=3)
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
    return render(request, 'add.html', locals())

@login_required(login_url='login')
def editPlanning(request, id):
    z = get_user(request).get_username()
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        cours = Cours.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        cours = Cours.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        cours = Cours.objects.filter(id_classe=3)
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
    return render(request, 'edit_planning.html', locals())

@login_required(login_url='login')
def delPlanning(request, id):
    planning = Planning.objects.get(id=id)
    planning.delete()
    return redirect(reverse("index"))


@login_required(login_url='login')
def ajout(request):
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
    else:
        classe = Classe.objects.filter(id=3)
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prenom_eleve = form.cleaned_data['prenom_eleve']
            nom_eleve = form.cleaned_data['nom_eleve']
            id_classe = form.cleaned_data['id_classe']
            email = form.cleaned_data['email']
            form.save()
            return redirect(reverse("index"))
    return render(request, 'ajout.html', locals())

@login_required(login_url='login')
def editEleve(request,id):
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
    else:
        classe = Classe.objects.filter(id=3)
    eleve = Eleve.objects.get(id=id)
    form = EleveForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            eleve.prenom_eleve= form.cleaned_data['prenom_eleve']
            eleve.nom_eleve = form.cleaned_data['nom_eleve']
            eleve.id_classe = form.cleaned_data['id_classe']
            eleve.save()
            return redirect(reverse("index"))
    return render(request, 'editeleve.html', locals())



###View pour prof

@login_required(login_url='login')
def liste(request):
    eleves  = Eleve.objects.all()
    return render(request, 'blog/liste.html', locals())

###View pour prof 

@login_required(login_url='login')
def liste_eleve_prof(request):
    eleves  = Eleve.objects.filter(id_classe=1)
    return render(request, 'listes_eleves.html', locals())

def liste_eleve_secretaire(request):
    eleves  = Eleve.objects.filter(id_classe=1)
    return render(request, 'secretaire_liste_elev.html', locals())

@login_required(login_url='login')
def liste_eleve_prof2(request):
    eleves2  = Eleve.objects.filter(id_classe=2)
    return render(request, 'listes_eleves.html', locals())

@login_required(login_url='login')
def liste_eleve_prof3(request):
    eleves3  = Eleve.objects.filter(id_classe=3)
    return render(request, 'listes_eleves.html', locals())






@login_required(login_url='login')
def liste_eleve(request):
    prof = Prof.objects.all()
    z = get_user(request).get_username()
    ip = 0
    iw = 0
    ic = 0
    ik = 0
    im = 0
    d = 0
    e = 0
    f = 0
    g = 0
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    classe = Classe.objects.all()
    res_profs = Responsable_Prof.objects.all()

    if (z == "Alioune"):
        plaquettes = Plaquette.objects.filter(id_classe=1)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=1)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=1)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=1)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=1)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=1)
        eleves = Eleve.objects.filter(id_classe=1)
        classes = Classe.objects.filter(id=1)

    elif (z == "Ibrahima"):
        plaquettes = Plaquette.objects.filter(id_classe=2)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=2)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=2)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=2)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=2)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=2)
        eleves = Eleve.objects.filter(id_classe=2)
        classes = Classe.objects.filter(id=2)
    else:
        plaquettes = Plaquette.objects.filter(id_classe=3)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=3)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=3)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=3)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=3)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=3)
        eleves = Eleve.objects.filter(id_classe=3)
        classes = Classe.objects.filter(id=3)

    profs = Prof.objects.all()
    return render(request, 'planningPlaquette.html', locals())


@login_required(login_url='login')
def delEleve(request,id):
    eleves = Eleve.objects.get(id=id)
    eleves.delete()
    return redirect(reverse("index"))

@login_required(login_url='login')
def notifications(request, id):
    notif = Notification.objects.filter(id_prof_recep=id)
    notif1 = Notification.objects.filter(id_prof_emmet=id)
    res = Prof.objects.all()
    a = datetime.datetime.now()
    c = id
    form = NotificationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            date = a
            contenu = form.cleaned_data['contenu']
            id_prof_recep = form.cleaned_data['id_prof_recep']
            id_prof_emmet = form.cleaned_data['id_prof_emmet']
            form.save()
    return render(request, 'notification.html', locals())


@login_required(login_url='login')
def Index_eleve(request):
    cours = Cours.objects.all()
    z = get_user(request).get_username()
    if (z == "Alioune"):
        classe = Classe.objects.filter(id=1)
        eleve = Eleve.objects.filter(id_classe=1)
        presabs = PresAbs.objects.filter(id_classe=1)
        cahiertexte = CahierTexte.objects.filter(id_classe=1)
    elif (z == "Ibrahima"):
        classe = Classe.objects.filter(id=2)
        eleve = Eleve.objects.filter(id_classe=2)
        presabs = PresAbs.objects.filter(id_classe=2)
        cahiertexte = CahierTexte.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        eleve = Eleve.objects.filter(id_classe=3)
        presabs = PresAbs.objects.filter(id_classe=3)
        cahiertexte = CahierTexte.objects.filter(id_classe=3)

    for j in presabs:
        j.nom_eleve = str(j.nom_eleve).replace("['", "").replace("'", "").replace("]", "")
    form = PresAbsenceForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            nom_eleve = request.POST.getlist('nom_eleve')
            id_cours = form.cleaned_data['id_cours']
            id_classe = form.cleaned_data['id_classe']
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            form.save()
            return redirect(reverse("index_eleve"))
    form = CahierTexteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            heure_cours = form.cleaned_data['heure_cours']
            date = form.cleaned_data['date']
            contenu = form.cleaned_data['contenu']
            id_classe = form.cleaned_data['id_classe']
            id_cours = form.cleaned_data['id_cours']
            form.save()
    return render(request, 'indexeleve.html', locals())



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
    return render(request, 'plaquette.html', locals())

@login_required(login_url='login')
def IndexPlaquetteSec(request):
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
    return render(request, 'plaquette_secret.html', locals())





@login_required(login_url='login')
def AjoutPlaquette(request):
    a = 0
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        pal = Plaquette.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        pal = Plaquette.objects.filter(id_classe=2)
        classe = Classe.objects.filter(id=2)
    else:
        pal = Plaquette.objects.filter(id_classe=3)
        classe = Classe.objects.filter(id=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'addplaquette.html', locals())
################ end plaquette prof#########################



@login_required(login_url='login')
def AjoutPlaquette1(request):
    a = 1
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        pal = Plaquette1.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        pal = Plaquette1.objects.filter(id_classe=2)
        classe = Classe.objects.filter(id=2)
    else:
        pal = Plaquette1.objects.filter(id_classe=3)
        classe = Classe.objects.filter(id=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'addplaquette.html', locals())


@login_required(login_url='login')
def AjoutPlaquette2(request):
    a = 2
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        pal = Plaquette2.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        pal = Plaquette2.objects.filter(id_classe=2)
        classe = Classe.objects.filter(id=2)
    else:
        pal = Plaquette2.objects.filter(id_classe=3)
        classe = Classe.objects.filter(id=3)
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
    return render(request, 'addplaquette.html', locals())

@login_required(login_url='login')
def AjoutPlaquette3(request):
    a = 3
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        pal = Plaquette3.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        pal = Plaquette3.objects.filter(id_classe=2)
        classe = Classe.objects.filter(id=2)
    else:
        pal = Plaquette3.objects.filter(id_classe=3)
        classe = Classe.objects.filter(id=3)
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
    return render(request, 'addplaquette.html', locals())

@login_required(login_url='login')
def AjoutPlaquette4(request):
    a = 4
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        pal = Plaquette4.objects.filter(id_classe=1)
        classe = Classe.objects.filter(id=1)
    elif (z == "Abdoulaye"):
        pal = Plaquette4.objects.filter(id_classe=2)
        classe = Classe.objects.filter(id=2)
    else:
        pal = Plaquette4.objects.filter(id_classe=3)
        classe = Classe.objects.filter(id=3)
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
    return render(request, 'addplaquette.html', locals())

@login_required(login_url='login')
def DelPlaquette(request, id):
    plaquettes = Plaquette.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("index"))

@login_required(login_url='login')
def DelPlaquette1(request, id):
    plaquettes = Plaquette1.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("index"))


@login_required(login_url='login')
def DelPlaquette2(request, id):
    plaquettes = Plaquette2.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("index"))

@login_required(login_url='login')
def DelPlaquette3(request, id):
    plaquettes = Plaquette3.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("index"))

@login_required(login_url='login')
def DelPlaquette4(request, id):
    plaquettes = Plaquette4.objects.get(id=id)
    plaquettes.delete()
    return redirect(reverse("index"))

@login_required(login_url='login')
def editPlaquette(request, id):
    a = 0
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        pal = Plaquette.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        pal = Plaquette.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        pal = Plaquette.objects.filter(id_classe=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'editplaquette.html', locals())

@login_required(login_url='login')
def editPlaquette1(request, id):
    a = 1
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        pal = Plaquette1.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        pal = Plaquette1.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        pal = Plaquette1.objects.filter(id_classe=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'editplaquette.html', locals())

@login_required(login_url='login')
def editPlaquette2(request, id):
    a = 2
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        pal = Plaquette2.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        pal = Plaquette2.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        pal = Plaquette2.objects.filter(id_classe=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'editplaquette.html', locals())

@login_required(login_url='login')
def editPlaquette3(request, id):
    a = 3
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        pal = Plaquette3.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        pal = Plaquette3.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        pal = Plaquette3.objects.filter(id_classe=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'editplaquette.html', locals())

@login_required(login_url='login')
def editPlaquette4(request, id):
    a = 4
    c = 0
    z = get_user(request).get_username()
    if (z == "Ahmed"):
        classe = Classe.objects.filter(id=1)
        pal = Plaquette4.objects.filter(id_classe=1)
    elif (z == "Abdoulaye"):
        classe = Classe.objects.filter(id=2)
        pal = Plaquette4.objects.filter(id_classe=2)
    else:
        classe = Classe.objects.filter(id=3)
        pal = Plaquette4.objects.filter(id_classe=3)
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
            return redirect(reverse("index"), locals())
    return render(request, 'editplaquette.html', locals())



@login_required(login_url='login')
def classe(request):
    prof = Prof.objects.all()
    z = get_user(request).get_username()
    ip = 0
    iw = 0
    ic = 0
    ik = 0
    im = 0
    d = 0
    e = 0
    f = 0
    g = 0
    res_profs = Responsable_Prof.objects.all()
    cours = Cours.objects.all()
    classe = Classe.objects.all()
    res_profs = Responsable_Prof.objects.all()

    if (z == "DIC1_GIT"):
        plaquettes = Plaquette.objects.filter(id_classe=1)
        ens = Enseigner.objects.all()

        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=1)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=1)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=1)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=1)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=1)
        eleves = Eleve.objects.filter(id_classe=1)
        classes = Classe.objects.filter(id=1)

    elif (z == "DIC2_GIT"):
        plaquettes = Plaquette.objects.filter(id_classe=2)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=2)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=2)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=2)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=2)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=2)
        eleves = Eleve.objects.filter(id_classe=2)
        classes = Classe.objects.filter(id=2)
    elif(z == "DIC3_GIT"):
        plaquettes = Plaquette.objects.filter(id_classe=3)
        for plaquette in plaquettes:
            ip = ip + 1
            for j in plaquettes:
                if j.ec != "":
                    d = 1
        plaquettes1 = Plaquette1.objects.filter(id_classe=3)
        for plaquette1 in plaquettes1:
            iw = iw + 1
            for j in plaquettes1:
                if j.ec != "":
                    e = 1
        plaquettes2 = Plaquette2.objects.filter(id_classe=3)
        for plaquette2 in plaquettes2:
            ic = ic + 1
            for j in plaquettes2:
                if j.ec != "":
                    f = 1
        plaquettes3 = Plaquette3.objects.filter(id_classe=3)
        for plaquette3 in plaquettes3:
            ik = ik + 1
            for j in plaquettes3:
                if j.ec != "":
                    g = 1
        plaquettes4 = Plaquette4.objects.filter(id_classe=3)
        for plaquette4 in plaquettes4:
            im = im + 1
        planning = Planning.objects.filter(id_classe=3)
        eleves = Eleve.objects.filter(id_classe=3)
        classes = Classe.objects.filter(id=3)

    profs = Prof.objects.all()
    return render(request, 'classe.html', locals())
