""" Handles URL requests """

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.staticfiles import finders
import django

from .businesslogic import get_session
from .businesslogic import add_item_to_inventory
from .businesslogic import remove_item_from_inventory
from .businesslogic import get_inventory_list
from .businesslogic import is_item_in_inventory
from .businesslogic import get_item_name
from .businesslogic import find_item
from .businesslogic import find_location
from .businesslogic import url_for_static_file
from .models import Location, Item


def index(request):
    """ Redirect to the first location. """
    return HttpResponseRedirect('/location/872308')


def display_location(request, location_id):
    location = find_location(request, location_id)
    
    if location:
        inventory = []
        inventory_list = get_inventory_list(request)
        for item in inventory_list:
            inventory.append((url_for_static_file(str(item) + ".jpg"), get_item_name(item))) 
        image_filename = location.locationidx + ".jpg"
        values = {'id': location.locationidx, 
                  'ort': location.locationname, 
                  'body': location.htmlbody, 
                  'inventory': inventory,
                  'image': url_for_static_file(image_filename)
                 }

        return render(request, 'location.html', values)
    else:
        return not_valid(request, location_id)


def add_item(request, item_id):
    item = add_item_to_inventory(request, item_id)
    if item:
        image_filename = item.itemidx + ".jpg"
        values = {'itemname': item.itemname, 
                  'body': item.htmlbody_add, 
                  'image': url_for_static_file(image_filename)}
                  
        return render(request, 'item.html', values)
    else:
        return HttpResponse("Gegenstand nicht gefunden.")


def remove_item(request, item_id):
    item = find_item(item_id)
    if item:
        if is_item_in_inventory(request, item_id):
            remove_item_from_inventory(request, item_id)
            return render(request, 'item.html', {'itemname': item.itemname, 'body': item.htmlbody_remove})
        else:
            return HttpResponse("Du hast den Gegenstand gar nicht. ")
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
    
