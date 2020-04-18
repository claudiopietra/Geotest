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
    inventory = get_inventory_list(request)
    locations = Location.objects.filter(locationidx=location_id)
    for location in locations:
        if location.in_inventory in inventory:
            return_location = location
            #return 'in inventory: ' + location.comment + ', ' + location.in_inventory + ', ' + str(inventory)
            break
            
        if location.not_in_inventory not in inventory:
            return_location = location
            return 'not in inventory: ' + location.comment + ', '+ location.not_in_inventory + ', ' + str(inventory)
            break

    return return_location


def get_inventory_list(request):
    return get_session(request)['inventory']


def find_item(item_id):
    """ finds an item and returns it, if found. """
    return_item = None
    items = Item.objects.filter(itemidx=item_id)
    if items:
        return_item = items[0]
    
    return return_item
    

def get_item_name(item_id):    
    """ Gets a name for an item-index. Returns '' if the 
        item is not found. """
    itemname = ""        
    item = find_item(item_id)
    if item:
        itemname = item.itemname
        
    return itemname


def add_item_to_inventory(request, item_id):
    """ Adds an item to the inventory. """
    item = find_item(item_id)
    if item:
        #---Item found, check if already in inventory
        inventory = get_inventory_list(request)
        if item_id not in inventory:
            #---somehow a direct append on the list stored in the session
            #   doesn't word - don't know why, but copying out and in again
            #   solves the problem.
            #---we store the string of the item_id, makes it easier to handle
            #   within lists and to compare it to textfields in the Location object.
            inventory.append(str(item_id))
            session = get_session(request)
            session['inventory'] = inventory
                
    return item


def remove_item_from_inventory(request, item_id):
    """ Removes an item from the inventory. """
    item = find_item(item_id)
    if item:
        inventory = get_inventory_list(request)
        if item_id not in inventory:
            inventory.remove(str(item_id))
            session = get_session(request)
            session['inventory'] = inventory
            
    return item

        
def is_item_in_inventory(request, item_id):
    """ Returns if an item_id is in the inventory. We store
        the id's as strings in the list. """
    return str(item_id) in get_inventory_list(request)


def get_inventory_name_list(request):
    inventorylist = get_session(request)['inventory']
    namelist = []
    for item_id in inventorylist:
        namelist.append(get_item_name(item_id))
   
    return namelist
        
