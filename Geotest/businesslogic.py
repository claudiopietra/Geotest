""" Businesslogic functions for the Geocache
    textadventure project. """

from .models import Location, Item
from django.conf import settings
import os 

#------------------------------------------------------------------------------
#   Session Handling
#------------------------------------------------------------------------------

def get_session(request):
    """ Initialize the session, if not already done. """
    session = request.session
    if not 'initialized' in session:
        #---Session should expire in 24h = 86400s
        session.set_expiry(86400)
        session['initialized'] = True
        session['inventory'] = []
        session['pastinventory'] = []
        session['wrongurls'] = 0

    return session

#------------------------------------------------------------------------------
#   Static File Handling
#------------------------------------------------------------------------------
    
def url_for_static_file(filename):
    """ Returns an URL for a static file. Returns
        empty if the file doesn't exist. """
    full_filename = os.path.join(settings.STATIC_ROOT, filename)
    if os.path.isfile(full_filename):
        return settings.STATIC_URL + filename
    else:
        return ""

#------------------------------------------------------------------------------
#   Location Handling
#------------------------------------------------------------------------------

    
def find_location(request, location_id):
    """ Finds the location with location_id, which matches
        the items in the inventory. """
    return_location = None
    inventory = get_inventory_list(request)
    locations = Location.objects.filter(locationidx=location_id)
    
    return "Anzahl Locations: " + str(len(locations))
    
    for location in locations:
        #---Locations can have a condition for items that were in the inventory.
        #   We have to check that as the first step, otherwise the "not in inventory"
        #   would kick in. 
        if location.was_in_inventory:
            past_inventory = get_past_inventory_list(request)
            if location.was_in_inventory in past_inventory:
                return_location = location
                break   

    for location in locations:
        #---Then we check if the location has an "in inventory" condition
        #   and return the first location found.
        if inventory and location.in_inventory:
            if location.in_inventory in inventory:
                return_location = location
                break
                
    for location in locations:            
        #---Then we check if the location has any "not in inventory" condition. 
        #   We return such a location, if an item specified in the location is 
        #   not in the inventory.
        if location.not_in_inventory:
            if location.not_in_inventory not in inventory:
                return_location = location
                break

    #---if we don't find a location with the inventory conditions, we return the 
    #   default location. 
    if not return_location:
        for location in locations:
            if location.default:
                return_location = location
                break

    return return_location


#------------------------------------------------------------------------------
#   Inventory Handling
#------------------------------------------------------------------------------


def get_inventory_list(request):
    return get_session(request)['inventory']
    

def get_past_inventory_list(request):
    return get_session(request)['pastinventory']


def find_item(item_id):
    """ finds an item and returns it, if found. """
    item = None
    items = Item.objects.filter(itemidx=item_id)
    if items:
        item = items[0]
    
    return item
    

def item_exists(item_id):
    """ Returns if an item with the item_id exists in the system. """
    if find_item(item_id):
        return True
    else:
        return False


def get_item_name(item_id):    
    """ Gets a name for an item-index. Returns '' if the 
        item is not found. """
    itemname = ""        
    item = find_item(item_id)
    if item:
        itemname = item.itemname
        
    return itemname

        
def is_item_in_inventory(request, item_id):
    """ Returns if an item_id is in the inventory. We store
        the id's as strings in the list. """
    return item_id in get_inventory_list(request)
    

def add_item_to_inventory(request, item_id):
    """ Adds an item to the inventory. """
    item = None
    if item_exists(item_id):
        if not is_item_in_inventory(request, item_id):
            inventory = get_inventory_list(request)
            #---somehow a direct append on the list stored in the session
            #   doesn't word - don't know why, but copying out and in again
            #   solves the problem.
            inventory.append(item_id)
            session = get_session(request)
            session['inventory'] = inventory
            
            item = find_item(item_id)

    return item


def remove_item_from_inventory(request, item_id):
    """ Removes an item from the inventory.
        The item is, however, stored in the 'pastinventory' list. """
    if item_exists(item_id):
        if is_item_in_inventory(request, item_id):
            inventory = get_inventory_list(request)

            inventory.remove(item_id)
            session = get_session(request)
            session['inventory'] = inventory

            pastinventory = session['pastinventory']
            pastinventory.append(item_id)
            session['pastinventory'] = pastinventory

            item = find_item(item_id)

    return item


def get_inventory_name_list(request):
    inventorylist = get_session(request)['inventory']
    namelist = []
    for item_id in inventorylist:
        namelist.append(get_item_name(item_id))
   
    return namelist
        
