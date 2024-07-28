from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        
        model=Post
        fields=['title','text','thumbnail','movie']
        
        def __str__(self):
            return self.title
    