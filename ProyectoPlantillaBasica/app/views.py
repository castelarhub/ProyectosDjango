# Create your views here.

from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

# Opcion 1
def inicio(request):
	ahora = datetime.now()
	t = get_template("miPlantilla.html")
	c = Context({"usuario":"Nelson Castelar","hora":ahora})
	html = t.render(c)
	return HttpResponse(html)

#Opcion 2
def inicio2(request):
	data = {"usuario":"Nelson C. ","hora":datetime.now()}
	return render_to_response("miPlantilla.html",data)
