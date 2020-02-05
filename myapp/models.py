from django.db import models

# Create your models here.

class Secretaire(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    mail=models.CharField(max_length=100)
    telephone=models.CharField(max_length=20)
    login=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


    def __str__(self):
        return self.nom


class Classe(models.Model):
    nom_classe=models.CharField(max_length=50)
    password_classe=models.CharField(max_length=50)
    login_classe = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Classe"
        ordering = ['nom_classe']

    def __str__(self):
        return self.nom_classe


class Eleve(models.Model):
    nom_eleve=models.CharField(max_length=50)
    prenom_eleve=models.CharField(max_length=50)
    id_classe=models.ForeignKey('Classe', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Eleve"
        ordering = ['nom_eleve']

    def __str__(self):
        return self.nom_eleve

class Responsable_Eleve(Eleve):
    login_res = models.CharField(max_length=40)
    pasword_res = models.CharField(max_length=40)


    class Meta:
        verbose_name = "Responsable de classe"
        ordering = ['login_res']

    def __str__(self):
        return self.nom_eleve

class CahierTexte(models.Model):
    heure_cours=models.CharField(max_length=50)
    date=models.DateTimeField()
    contenu=models.TextField()
    id_eleve=models.ForeignKey('Eleve', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cahier de texte"
        ordering = ['date']

    def __str__(self):
        return self.contenu


class Prof(models.Model):
    nom_prof=models.CharField(max_length=50)
    prenom_prof=models.CharField(max_length=50)
    mail_prof=models.CharField(max_length=50)
    login_prof=models.CharField(max_length=50)
    password_prof=models.CharField(max_length=50)

    def __str__(self):
        return self.prenom_prof


class Responsable_Prof(Prof):
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    def __str__(self):
        return self.prenom_prof


class Cours(models.Model):
    nom_cours=models.CharField(max_length=50)
    duree=models.CharField(max_length=50)
    date=models.DateField()
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_cours

class Notification(models.Model):
    date=models.DateTimeField()
    contenu=models.TextField()
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)

    def __str__(self):
        return self.contenu

class Enseigner(models.Model):
    id_classe=models.ForeignKey('Classe', on_delete=models.CASCADE)
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_classe


class PresAbs(models.Model):
    id_eleve=models.ForeignKey('Eleve', on_delete=models.CASCADE)
    id_cours=models.ForeignKey('Cours', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.id_eleve

class Planning(models.Model):
    heure = models.CharField(max_length=7, null=True)
    moduleLundi = models.CharField(max_length=30, blank=True)
    moduleMardi = models.CharField(max_length=30, blank=True)
    moduleMercredi = models.CharField(max_length=30, blank=True)
    moduleJeudi = models.CharField(max_length=30, blank=True)
    moduleVendredi = models.CharField(max_length=30, blank=True)
    moduleSamedi = models.CharField(max_length=30, blank=True)
    id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Planning"


    def __str__(self):
        return self.heure