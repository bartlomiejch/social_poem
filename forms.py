from social_poem.models import Stropha
from django import forms

class StrophaAddForm(forms.Form):
	add_stropha = forms.CharField(max_length=200)
