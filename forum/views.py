from django.shortcuts import render, get_object_or_404
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


def single_post(request, post_id):
    """ A view to show individual product details """

    post = get_object_or_404(ForumPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'forum/single_post.html', context)

