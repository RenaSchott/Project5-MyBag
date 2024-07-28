from django import forms
from .models import ForumPostCategory, ForumPost, ForumComment


class PostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = ForumPostCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in category]

        self.fields['entry_cat'].choices = friendly_names


class CommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ('content',)
