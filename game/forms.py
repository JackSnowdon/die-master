from django import forms
from .models import *

class DarkGameForm(forms.ModelForm):

    class Meta:
        model = DarkHeresyGame
        exclude = ['dm']


class DarkRollForm(forms.ModelForm):

    class Meta:
        model = DarkDieRoll
        fields = '__all__'


class DarkRollRoller(forms.ModelForm):

    class Meta:
        model = DarkDieRoll
        fields = ['roll_amount']