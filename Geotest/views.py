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
        return not_valid(request, location_id)


def not_valid(request, entered_url):
    session = get_session(request)
    session['wrongurls'] += 1
    if session['wrongurls'] >= 15:
        session.flush()
        return HttpResponse('Du hast Dich offensichtlich (virtuell) verlaufen, wir schlagen vor, dass Du nochmals von vorne anfaengst')
    else:
        return HttpResponse('hier ist nichts. kommt von not_valid. get_session lief. Anzahl fehlerhaften Aufrufe: %s' %str(session['wrongurls']))
    
