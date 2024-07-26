from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class ForumPostCategory(models.Model):
    """ Defines category of forum post """
    entry_cat = models.CharField(max_length=200, unique=True)
    friendly_name = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.entry_cat

    def get_friendly_name(self):
        return self.friendly_name


class ForumPost(models.Model):
    """ Creates forum post """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="author")
    entry_cat = models.ForeignKey(
        ForumPostCategory, on_delete=models.CASCADE, related_name="cat")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    short = models.TextField(default="an_excerpt")

    class Meta:
        ordering = ["created_on", "approved"]

    def __str__(self):
        return self.title


class ForumComment(models.Model):
    """ Stores a single user comment """
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="writer")
    comment = models.ForeignKey(
        ForumPost, on_delete=models.CASCADE, related_name="comments")
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["created_on", "approved"]

    def __str__(self):
        return f"Comment added by {self.writer}"
