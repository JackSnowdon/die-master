from django import forms
from .models import *

class DarkGameForm(forms.ModelForm):

    class Meta:
        model = DarkHeresyGame
        exclude = ['dm']
