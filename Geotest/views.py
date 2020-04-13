""" Handles URL requests """

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import django

from Geotest.models import Location


def index(request):
    """ Redirect to the first location. """

    return HttpResponseRedirect('/location/12345')


def display_location(request, location_id):
    locations = Location.objects.filter(locationidx=location_id)
    if len(locations):
        location = locations[0]
        return render(request, 'index.html', {'title': location.locationname, 'body': location.htmlbody})
    else:
        return HttpResponse('nicht gefunden, Nummer ist %i' %location_id)


def not_valid(request, entered_url):
    return HttpResponse('hier ist nichts.')