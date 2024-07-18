from django.shortcuts import render

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def privacy(request):
    """
    A view to retun the privacy policy page
    """
    return render(request, 'home/privacy.html')
