from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """
    renders about page
    """
    return render(request, 'home/about.html')


def privacy(request):
    """
    A view to retun the privacy policy page
    """
    return render(request, 'home/privacy.html')
