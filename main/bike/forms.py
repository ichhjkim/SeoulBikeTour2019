from django import forms
from .models import Spot, Bicycle

class SpotForm(forms.ModelForm):

    class Meta:
        model = Spot
        fields = '__all__'

class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = '__all__'
