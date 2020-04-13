""" Businesslogic functions for the Geocache
    textadventure project. """
    
def get_session(request):
    session = request.session
    if not session.get('initialized', False):
        #---Session should expire in 24h = 86400s
        session.set_expiry(86400)
        session['initialized'] = True
        session['inventory'] = []
        session['wrongurls'] = 0

    return session
