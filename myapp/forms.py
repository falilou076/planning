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
    class Meta:
        model = PresAbs
        fields = '__all__'
