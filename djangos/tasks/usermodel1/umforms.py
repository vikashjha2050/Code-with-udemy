from django import forms
from django.contrib.auth.models import User
from usermodel1.models import userinfo

class userform(forms.ModelForm):
     password=forms.CharField(widget=forms.PasswordInput())
     class Meta():
         model=User
         fields=('username','email','password')

class userinfo1(forms.ModelForm):
    class Meta():
        model=userinfo
        fields=('website','profile_pic')
