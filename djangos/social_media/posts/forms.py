from django import forms
from posts.models import post

class PostForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ('groupname', 'postcontent','user')
        widgets = {'user': forms.HiddenInput()}
