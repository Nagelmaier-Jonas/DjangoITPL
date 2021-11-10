import urllib.request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from Web.models import *
from .forms import LogForm
from urllib import *

def get_station(request):
    log = Log()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            log.message = form.cleaned_data['message']
            log.createdAt = form.cleaned_data['createdAt']
            log.station_id = form.cleaned_data['station']
            log.save()
            # redirect to a new URL:
            return HttpResponseRedirect('test')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogForm()
    return render(request, 'log.html', {'form': form})