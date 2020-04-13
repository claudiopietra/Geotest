""" Businesslogic functions for the Geocache
    textadventure project. """

from .models import Location, Item

def get_session(request):
    """ Initialize the session, if not already done. """
    session = request.session
    if not session.get('initialized', False):
        #---Session should expire in 24h = 86400s
        session.set_expiry(86400)
        session['initialized'] = True
        session['inventory'] = []
        session['wrongurls'] = 0

    return session
    

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
    itemname = get_item_name(item_idx)
    if itemname:
        session = get_session(request)
        #---Item found, check if already in inventory
        if item_id not in session['inventory']:
            session['inventory'].append(item_id)
                
    return itemname


def get_inventory_name_list(request):
    inventorylist = get_session(request)['inventory']
    namelist = []
    for item_id in inventorylist:
        namelist.append(get_item_name(item_id))
   
    return namelist
        
