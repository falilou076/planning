from django import forms
from .models import Eleve, Planning


class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = '__all__'
