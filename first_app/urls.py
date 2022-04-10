# este archivo url se crea para tener las url de esta aplicaion dentro de la app y no confundirlas con otras url de
#otra posible aplicacion

from django.urls import path
from first_app import views


urlpatterns = [
    path('index/',views.index),
  
]