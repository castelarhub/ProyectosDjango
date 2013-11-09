# Create your views here.
from django.http import HttpResponse

def inicio(request):
	return HttpResponse("Hola Bienvenido, esta es la pagina de inicio!!!")	

def hola(request):
	return HttpResponse("Hola Mundo en texto!!!")

def hola2(request):
	html = HttpResponse("<html><body><h1>Hola mundo en html!!!</h1></body></html>")
	return html

def hola3(request,nombre_usuario):
	html = HttpResponse("<html><body><h1>Hola %s bienvenido!!!</h1></body></html>" %nombre_usuario)
	return html	

def otro(request):
	return HttpResponse("Este mensaje se muestra si el patron de la url no concuerda con los configurados.!!!")	