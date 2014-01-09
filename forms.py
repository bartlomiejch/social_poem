from social_poem.models import Stropha
from django import forms

class StrophaAddForm(forms.Form):
	added_strofa = forms.CharField(max_length=200)
