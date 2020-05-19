from django import forms
from .models import *

class DarkBaseForm(forms.ModelForm):

    class Meta:
        model = DarkHeresyBase
        exclude = ['created_by']
