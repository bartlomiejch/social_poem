from django.shortcuts import render_to_response
from social_poem.models import Stropha
from django.template import Context, loader
from django.core.context_processors import csrf 
from django.http import HttpResponse
from social_poem.forms import StrophaAddForm


def poem(request):
	if request.method == "POST":
		form = StrophaAddForm(request.POST)
		if form.is_valid():
			my_model = Stropha()
			my_model.stropha = form.cleaned_data['add_stropha']
			my_model.save()
			
	form = StrophaAddForm()
	poetry = Stropha.objects.all()
	c ={'poetry': poetry, 'form':form}
	c.update(csrf(request))
	return render_to_response('social_poem/social_poem.html', c)
