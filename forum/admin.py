from django.contrib import admin
from .models import ForumPostCategory, ForumPost, ForumComment


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'entry_cat', 'created_on', 'content',
        'slug', 'status', 'approved', 'short')
    search_fields = ['title', 'author', 'entry_cat']
    list_filter = ('status', 'author', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters.
    """
    list_display = (
        'content', 'created_on', 'writer', 'comment', 'updated_on', 'approved')
    list_filter = ('comment', 'created_on', 'approved')
    search_fields = ['comment']


@admin.register(ForumPostCategory)
class ForumPostCategoryAdmin(admin.ModelAdmin):
    pass
