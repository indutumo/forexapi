from django import forms
from .models import *

class ForexRateForm(forms.Form):
    base_currency = forms.CharField()
    target_currency = forms.CharField()