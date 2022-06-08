from django import forms
from Web.models import Station, Configuration

def getStations():
    for o in Station.objects.all():
        yield (o.id, o.name)

def getConfigurations():
    for o in Configuration.objects.all():
        yield (o.id, o.command)

class StationHasConfigurationJTForm(forms.Form):
    def __init__(self, *args, request=None, **kwargs):
        super(StationHasConfigurationJTForm, self).__init__(*args, **kwargs)
        self.fields["stationId"].choices = getStations()
        self.fields["configurationId"].choices = getConfigurations()

    stationId = forms.ChoiceField(choices=getStations())
    configurationId = forms.ChoiceField(choices=getConfigurations())
