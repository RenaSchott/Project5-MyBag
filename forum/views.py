from django.shortcuts import render
from django.views import generic

from .models import ForumPostCategory, ForumPost, ForumComment


def forum(request):
    """ A view to return the forum page """

    return render(request, 'forum/forum.html')
