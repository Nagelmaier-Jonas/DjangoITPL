from django import forms
from Web.models import Station, StationHasConfigurationJT, Configuration


class StationHasConfigurationJTForm(forms.Form):
    stationId = forms.ChoiceField(choices=[(o.id, o.name)for o in Station.objects.all()])
    configurationId = forms.ChoiceField(choices=[(o.id, o.command)for o in Configuration.objects.all()])
