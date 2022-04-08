from django.http import HttpResponse
from django.shortcuts import render  #importamos la libreria https response para la respuesta

def home (request):


    return HttpResponse("home")

def  servicios (request):
    
    return render(request, (" first_app.tenplate/servicios.html"))

def tienda (request):

    return HttpResponse("tienda")

def blog (request):

    return HttpResponse("blog")

def contac(request):

    return HttpResponse("contac")