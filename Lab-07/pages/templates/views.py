from django.shortcuts import render
from django.http import HttpResponse

# Asegúrate de tener esta función definida
def about(request):
    return HttpResponse("Acerca de nosotros") # O render(request, 'about.html')
