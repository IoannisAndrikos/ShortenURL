from django import forms
from requests.api import post

class getURL(forms.Form):
    text_url = forms.CharField(label='URL')