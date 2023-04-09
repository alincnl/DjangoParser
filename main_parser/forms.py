from django import forms

class URLForm(forms.Form):
    URL = forms.CharField(max_length=255)
