""" Businesslogic functions for the Geocache
    textadventure project. """

from .models import Location, Item

def get_session(request):
    """ Initialize the session, if not already done. """
    session = request.session
    if not 'initialized' in session:
        #---Session should expire in 24h = 86400s
        session.set_expiry(86400)
        session['initialized'] = True
        session['inventory'] = []
        session['wrongurls'] = 0

    return session
    
    
def find_location(request, location_id):
    """ Finds the location with location_id, which matches
        the items in the inventory. """
    return_location = None
    inventory = get_session(request)['inventory']
    locations = Location.objects.filter(locationidx=location_id)
    for location in locations:
        if location.in_inventory in inventory:
            return_location = location
            return location.comment, location.in_inventory
            break
            
        if location.not_in_inventory not in inventory:
            return_location = location
            return location.comment, location.in_inventory
            break

    return return_location


def get_item_name(item_id):    
    """ Gets a name for an item-index. Returns '' if the 
        item is not found. """
    itemname = ""
    items = Item.objects.filter(itemidx=item_id)
    if items:
        itemname = items[0].itemname
        
    return itemname


def add_item_to_inventory(request, item_id):
    """ Adds an item to the inventory. """
    itemname = get_item_name(item_id)
    if itemname:
        session = get_session(request)
        #---Item found, check if already in inventory
        if item_id not in session['inventory']:
            #---somehow a direct append on the list stored in the session
            #   doesn't word - don't know why, but copying out and in again
            #   solves the problem. 
            item_list = session['inventory']
            item_list.append(item_id)
            session['inventory'] = item_list
                
    return itemname


def get_inventory_name_list(request):
    inventorylist = get_session(request)['inventory']
    namelist = []
    for item_id in inventorylist:
        namelist.append(get_item_name(item_id))
   
    return namelist
        
