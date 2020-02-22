from django import forms
from .models import *


class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = '__all__'

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

class CahierTexteForm(forms.ModelForm):
    class Meta:
        model = CahierTexte
        fields = '__all__'

class PresAbsenceForm(forms.ModelForm):
    nom_eleve = forms.CharField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = PresAbs
        fields = '__all__'

class PlaquetteForm(forms.ModelForm):
    class Meta:
        model = Plaquette
        fields = '__all__'

class Plaquette1Form(forms.ModelForm):
    class Meta:
        model = Plaquette1
        fields = '__all__'

class Plaquette2Form(forms.ModelForm):
    class Meta:
        model = Plaquette2
        fields = '__all__'

class Plaquette3Form(forms.ModelForm):
    class Meta:
        model = Plaquette3
        fields = '__all__'

class Plaquette4Form(forms.ModelForm):
    class Meta:
        model = Plaquette4
        fields = '__all__'