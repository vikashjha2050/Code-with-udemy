from django import forms
from basicforms.models import usertable
from django.forms import ModelForm

class userform(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=usertable
        fields='__all__'
