from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User
# Create your models here.

class Secretaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Liaison 0netoOne vers le model User
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    mail=models.CharField(max_length=100)
    telephone=models.CharField(max_length=20)

    class Meta :
        verbose_name_plural = "Secretaire"


    def __str__(self):
        return " {0}".format(self.user.username)


class Classe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liaison 0netoOne vers le model User
    nom_classe=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Classe"
        ordering = ['nom_classe']

    def __str__(self):
        return "{0}".format(self.user.username)


class Eleve(models.Model):
    nom_eleve=models.CharField(max_length=50)
    prenom_eleve=models.CharField(max_length=50)
    id_classe=models.ForeignKey('Classe', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Eleve"
        ordering = ['nom_eleve']


    def __str__(self):
        return self.prenom_eleve

class Responsable_Eleve(Eleve):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liaison 0netoOne vers le model User

    class Meta:
        verbose_name_plural = "Responsable de classe"
        ordering = ['prenom_eleve']

    def __str__(self):
        return " {0}".format(self.user.username)

class CahierTexte(models.Model):
    heure_cours=models.CharField(max_length=50)
    date=models.DateField()
    contenu=models.TextField()
    id_eleve=models.ForeignKey('Responsable_Eleve', on_delete=models.CASCADE)
    id_cours=models.ForeignKey('Cours', on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Cahier de texte"
        ordering = ['date']

    def __str__(self):
        return self.contenu


class Prof(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liaison 0netoOne vers le model User
    nom_prof=models.CharField(max_length=50)
    prenom_prof=models.CharField(max_length=50)
    mail_prof=models.CharField(max_length=50)
    classe=models.ManyToManyField(Classe)

    class Meta :
        verbose_name_plural = "Professeur"

    def __str__(self):
        return "{0}".format(self.user.username)

class Responsable_Prof(Prof):
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    class Meta :
        verbose_name_plural = "Responsable pédagogique"

    def __str__(self):
        return self.prenom_prof


class Cours(models.Model):
    nom_cours=models.CharField(max_length=50)
    duree=models.CharField(max_length=50)
    date=models.DateField()
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    class Meta :
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.nom_cours

class Notification(models.Model):
    date=models.DateTimeField(default=timezone.now, verbose_name='date d envoi')
    contenu=models.TextField()
    id_prof_emmet= models.IntegerField()
    id_prof_recep = models.ForeignKey('Prof', on_delete=models.CASCADE)

    class Meta :
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.contenu

class Enseigner(models.Model):
    id_classe=models.ForeignKey('Classe', on_delete=models.CASCADE)
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)

    class Meta :
        verbose_name_plural = "Enseigner"



class PresAbs(models.Model):
    nom_eleve=models.CharField(max_length=400)
    id_cours=models.ForeignKey('Cours', on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.CharField(max_length=10)

    class Meta :
        verbose_name_plural = "Absences"
        ordering = ['date']
    def __str__(self):
        return self.nom_eleve

class Planning(models.Model):
    heure = models.CharField(max_length=7, null=True)
    moduleLundi = models.CharField(max_length=30, blank=True)
    moduleMardi = models.CharField(max_length=30, blank=True)
    moduleMercredi = models.CharField(max_length=30, blank=True)
    moduleJeudi = models.CharField(max_length=30, blank=True)
    moduleVendredi = models.CharField(max_length=30, blank=True)
    moduleSamedi = models.CharField(max_length=30, blank=True)
    id_prof=models.ForeignKey('Responsable_Prof', on_delete=models.CASCADE)
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Planning"


    def __str__(self):
        return self.heure


class Plaquette(models.Model):
    ue = models.CharField(max_length=40, blank=True)
    ec = models.CharField(max_length=30)
    cm = models.CharField(max_length=3)
    tpd = models.CharField(max_length=3)
    ttal = models.CharField(max_length=3)
    tpe = models.CharField(max_length=3)
    ects = models.CharField(max_length=3)
    total_Ects = models.CharField(max_length=3, blank=True)
    coefs = models.CharField( max_length=2, blank=True)
    coefs_details = models.IntegerField()


    class Meta:
        verbose_name = "Plaquette"

    def __str__(self):
        return self.ec

class Plaquette1(models.Model):
    ue = models.CharField(max_length=40, blank=True)
    ec = models.CharField(max_length=30)
    cm = models.CharField(max_length=3)
    tpd = models.CharField(max_length=3)
    ttal = models.CharField(max_length=3)
    tpe = models.CharField(max_length=3)
    ects = models.CharField(max_length=3)
    total_Ects = models.CharField(max_length=3, blank=True)
    coefs = models.CharField( max_length=2, blank=True)
    coefs_details = models.IntegerField()


    class Meta:
        verbose_name = "Plaquette1"

    def __str__(self):
        return self.ec

class Plaquette2(models.Model):
    ue = models.CharField(max_length=40, blank=True)
    ec = models.CharField(max_length=30)
    cm = models.IntegerField()
    tpd = models.IntegerField()
    ttal = models.IntegerField()
    tpe = models.IntegerField()
    ects = models.IntegerField()
    total_Ects = models.CharField(max_length=3, blank=True)
    coefs = models.CharField( max_length=2, blank=True)
    coefs_details = models.IntegerField()


    class Meta:
        verbose_name = "Plaquette2"

    def __str__(self):
        return self.ec

class Plaquette3(models.Model):
    ue = models.CharField(max_length=40, blank=True)
    ec = models.CharField(max_length=30)
    cm = models.IntegerField()
    tpd = models.IntegerField()
    ttal = models.IntegerField()
    tpe = models.IntegerField()
    ects = models.IntegerField()
    total_Ects = models.CharField(max_length=3, blank=True)
    coefs = models.CharField( max_length=2, blank=True)
    coefs_details = models.IntegerField()


    class Meta:
        verbose_name = "Plaquette3"

    def __str__(self):
        return self.ec

class Plaquette4(models.Model):
    ue = models.CharField(max_length=40, blank=True)
    ec = models.CharField(max_length=30)
    cm = models.IntegerField()
    tpd = models.IntegerField()
    ttal = models.IntegerField()
    tpe = models.IntegerField()
    ects = models.IntegerField()
    total_Ects = models.CharField(max_length=3, blank=True)
    coefs = models.CharField( max_length=2, blank=True)
    coefs_details = models.IntegerField()


    class Meta:
        verbose_name = "Plaquette4"

    def __str__(self):
        return self.ec