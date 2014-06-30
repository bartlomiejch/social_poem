from django import forms

from social_poem.models import Stropha

class StrophaAddForm(forms.Form):
	add_stropha = forms.CharField(max_length=200)
