from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import django

from Geotest.models import Ort


def index(request):

    if not 'Name' in request.session:
        return HttpResponseRedirect('/entername/')

    title = "Amadeo und Claudios Geocache Adventure"
    body ="""Willkommen %s, hier startet Dein Abenteuer!
             Du wirst viele gefährliche Dinge erleben bis Du dir Prinzessin aus fen Fängen des Drachen befreien kannst.
             Bist Du mutig genug?
          """ %request.session['Name']

    return render(request, 'index.html', {'title': title, 'body': body})


def entername(request):

    from .forms import NameInputForm

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['Name'] = form.cleaned_data['players_name']
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameInputForm()

    return render(request, 'entername.html', {'form': form})


def display_ort(request, ort_id):
    orte = Ort.objects.filter(ortidx=ort_id)
    if len(orte):
        ort = orte[0]
        return render(request, 'index.html', {'title': ort.ortname, 'body': ort.htmlbody})
    else:
        return HttpResponse('nicht gefunden, Nummer ist %i' %ort_id)


def not_valid(request, entered_url):
    return HttpResponse('hier ist nichts.')