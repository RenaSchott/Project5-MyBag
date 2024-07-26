from django.shortcuts import render
from django.contrib import messages


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


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "errors/500.html", status=500)
