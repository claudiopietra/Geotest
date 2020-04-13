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


def add_item_to_inventory(request, item_id)
    """ Adds an item to the inventory. """
    itemname = ""
    items = Item.objects.filter(itemidx=item_id)
    if len(items):
        #---Item found, check if already in inventory
        if item_id not in session['inventory']:
            session['inventory'].append(item_id)
                itemname = items[0].itemname
                
    return itemname

 