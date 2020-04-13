""" Handles URL requests """

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import django

from .businesslogic import get_session
from .models import Location, Item

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
        
        
def add_item(request, item_id):
    items = Item.objects.filter(itemidx=item_id)
    if len(items):
        session["inventory"].append(item_id)
        return HttpResponse("Du hast ein %s erhalten" %item.itemname)
    else:
        return HttpResponse("Gegensatz nicht gefunden.")


def remove_item(request, item_id):
    pass


def not_valid(request, entered_url):
    session = get_session(request)
    session['wrongurls'] += 1
    if session['wrongurls'] >= 15:
        session.flush()
        #---TODO: mit einem Template zurueckgeben
        return HttpResponse('Du hast Dich offensichtlich (virtuell) verlaufen, wir schlagen vor, dass Du nochmals von vorne anfaengst')
    else:
        #---TODO: mit einem Template zurueckgeben
        return HttpResponse('hier ist nichts. kommt von not_valid. get_session lief. Anzahl fehlerhaften Aufrufe: %s' %str(session['wrongurls']))
    
