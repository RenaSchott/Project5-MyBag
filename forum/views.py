from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ForumPostCategory, ForumPost, ForumComment
from .forms import PostForm, CommentForm


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
    """ A view to show individual post details """

    queryset = ForumPost.objects.filter(status=1)
    post = get_object_or_404(ForumPost, pk=post_id)
    comments = post.comments.all().order_by("-created_on")
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.writer = request.user
            comment.comment = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()


    context = {
        'post': post,
        "comments": comments,
        "comment_form": comment_form
    }

    return render(request, 'forum/single_post.html', context)


@login_required
def add_post(request):
    """
    Add a post to the store with double security with either 
    redirection to login page or to home page with error message
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """
    Edit a post in the store with double security with either 
    redirection to login page or to home page with error message
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.name}')

    template = 'posts/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """
    Delete a post from the store with double security with either 
    redirection to login page or to home page with error message
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('posts'))
