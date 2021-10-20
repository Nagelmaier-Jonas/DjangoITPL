from django import forms
from Web.models import *


class LogForm(forms.Form):
    message = forms.CharField()
    createdAt = forms.DateTimeField()
    station = forms.IntegerField()
