""" Handles URL requests """

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import django

from .businesslogic import get_session
from .businesslogic import add_item_to_inventory
from .businesslogic import remove_item_from_inventory
from .businesslogic import get_inventory_name_list
from .businesslogic import get_inventory_list
from .businesslogic import is_item_in_inventory
from .businesslogic import get_item_name
from .businesslogic import find_location
from .models import Location, Item

def index(request):
    """ Redirect to the first location. """
    return HttpResponseRedirect('/location/872308')


def display_location(request, location_id):
    #return HttpResponse(find_location(request, location_id))
    location = find_location(request, location_id)
    
    if location:
        inventory_list = get_inventory_name_list(request)
        return render(request, 'location.html', {'ort': location.locationname, 'body': location.htmlbody, 'inventory_list': inventory_list})
    else:
        return not_valid(request, location_id)
        
        
def add_item(request, item_id):
    itemname = add_item_to_inventory(request, item_id)
    if itemname:     
        return HttpResponse("Du hast ein %s erhalten" %itemname)
    else:
        return HttpResponse("Gegenstand nicht gefunden.")


def remove_item(request, item_id):
    itemname = get_item_name(item_id)
    if itemname:
        if is_item_in_inventory(request, item_id):
            remove_item_from_inventory(request, item_id)
            HttpResponse("Du hast ein %s gegeben" %itemname)
        else:
            HttpResponse("Du hast den Gegenstand gar nicht. ")
    else:
        return HttpResponse("Gegenstand nicht gefunden.")


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
    
