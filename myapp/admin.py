from django.contrib import admin
from .models import *

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
admin.site.register(Planning)
admin.site.register(Responsable_Eleve)
admin.site.register(Responsable_Prof)
