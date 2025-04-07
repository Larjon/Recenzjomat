from django import forms
from .models import Recenzja, Ksiazka

class RecenzjaForm(forms.ModelForm):
    class Meta:
        model = Recenzja
        fields = ['tresc', 'ocena']
        widgets = {
            'ocena': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class KsiazkaForm(forms.ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'opis', 'kategorie']


class RecenzjaForm(forms.ModelForm):
    class Meta:
        model = Recenzja
        fields = ['tresc', 'ocena']
        widgets = {
            'tresc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ocena': forms.NumberInput(attrs={
                'class': 'form-control w-auto',
                'min': 1,
                'max': 5
            }),
        }
