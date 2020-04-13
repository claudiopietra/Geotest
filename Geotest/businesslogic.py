""" Businesslogic functions for the Geocache
    textadventure project. """
    
def get_session(request):
    if "initialized" not in request.session:
        request.session['initialized'] = True
        request.session['inventory'] = []
        request.session['wrongpages'] = 0
        
    return request.session