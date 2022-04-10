from django.http import HttpResponse
from django.shortcuts import render  #importamos la libreria https response para la respuesta

def index (request):


    return render(request,"first_app/index.html")


