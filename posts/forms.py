from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Post
        fields = [
            'topic',
            'title', 
            'content',
            'image',
        ]
