from django.shortcuts import render
from django.views import generic

from .models import ForumPostCategory, ForumPost, ForumComment
from .forms import ForumPostCategoryForm


def forum(request):
    """ A view to return the forum page """
    posts = ForumPost.objects.all()
    forumpostcategorys = None 


    if 'forumpostcategory' in request.GET:
        category = ForumPostCategory.objects.get(entry_cat=request.GET['forumpostcategory'])
        posts = posts.filter(entry_cat__exact=category.pk)
        forumpostcategorys = ForumPostCategory.objects.filter(entry_cat__in=request.GET['forumpostcategory'])

    context ={
        "posts": posts,
        'current_forumpostcategorys': forumpostcategorys,
    }

    return render(request, 'forum/forum.html', context)
