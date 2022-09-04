from unicodedata import name
from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=16)
    password = forms.CharField(max_length=16)