from django.shortcuts import render
from django.views import generic

from .models import ForumPostCategory, ForumPost, ForumComment
from .forms import ForumPostCategoryForm


def forum(request):
    """ A view to return the forum page """
    post = ForumPost.objects.all()
    forumpostcategorys = None 

    if 'forumpostcategory' in request.GET:
        forumpostcategorys = request.GET['forumpostcategorys'].split(',')
        forumpost = forumposts.filter(forumpostcategory__entry_cat__in=forumpostcategorys)
        forumpostcategorys = ForumPostCategory.objects.filter(entry_cat__in=forumpostcategorys)

    context ={
        "post": post,
        'current_forumpostcategorys': forumpostcategorys,
    }

    return render(request, 'forum/forum.html', context)
