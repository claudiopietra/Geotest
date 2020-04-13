""" Handles URL requests """

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import django

from .businesslogic import get_session
from .models import Location

def index(request):
    """ Redirect to the first location. """
    return HttpResponseRedirect('/location/12345')


def display_location(request, location_id):
    locations = Location.objects.filter(locationidx=location_id)
    if len(locations):
        location = locations[0]
        return render(request, 'index.html', {'title': location.locationname, 'body': location.htmlbody})
    else:
        not_valid(request, location_id)


def not_valid(request, entered_url):
    session = get_session(request)
    return HttpResponse('hier ist nichts. Session=%s' %str(session))
    
    #session['wrongurls'] += 1
    #return HttpResponse('hier ist nichts. Anzahl Fehlversuche: %s. Session=%s' %(str(session['wrongurls']), str(session)))