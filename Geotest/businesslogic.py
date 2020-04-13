""" Businesslogic functions for the Geocache
    textadventure project. """
    
def get_session(request):
    session = request.session
    if not session.get('initialized', False):
        session['initialized'] = True
        session['inventory'] = []
        session['wrongurls'] = 0
        
    return session