import json
from urllib import request, parse
import urllib
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import StationHasConfigurationJTForm

from Web.models import *

from urllib import *


@csrf_exempt
def get_station(request, url):
    station = Station()
    try:
        station.url = url
        station.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("ok")


@csrf_exempt
def set_command(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StationHasConfigurationJTForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            command = StationHasConfigurationJT()
            # process the data in form.cleaned_data as required
            command.stationId_id = form.cleaned_data['stationId']
            command.configurationId_id = form.cleaned_data['configurationId']
            command.save()
            config = Configuration.objects.get(id=command.configurationId_id)
            data = parse.urlencode(
                {'command': config.command, 'delay': config.delay, 'stationId': command.stationId_id}).encode()
            url = Station.objects.get(id=command.stationId_id).url
            resp = urllib.request.urlopen('http://' + url + ':8001/getconfiguration', data)
            # redirect to a new URL:
            return HttpResponse('ok')
# if a GET (or any other method) we'll create a blank form
    else:
        form = StationHasConfigurationJTForm()
    return render(request, 'configuration.html', {'form': form})



@csrf_exempt
def get_log(request):
    station = Station()
    station = Station.objects.get(id=request.POST.get('stationId'))
    station.save()

    config = Configuration()
    config = Configuration.objects.get(command=request.POST.get('command'), delay=request.POST.get('delay'))
    config.save()

    station_jt = StationHasConfigurationJT()
    station_jt.stationId = station
    station_jt.configurationId = config
    station_jt.save()

    log = Log()
    log.message = request.POST.get("message")
    log.createdAt = request.POST.get("createdAt")
    log.station_jt = station_jt

    log.save()
    # redirect to a new URL:
    return HttpResponseRedirect('Hello')
