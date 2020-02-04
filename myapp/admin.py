from django.contrib import admin
from .models import Secretaire,Classe,Eleve,CahierTexte,Prof,Cours,Notification,Enseigner,PresAbs

# Register your models here.
admin.site.register(Secretaire)
admin.site.register(Eleve)
admin.site.register(Classe)
admin.site.register(CahierTexte)
admin.site.register(Prof)
admin.site.register(Cours)
admin.site.register(Notification)
admin.site.register(Enseigner)
admin.site.register(PresAbs)
