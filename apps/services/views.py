from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def services(request):
    # Esta sí es privada (usando el decorador o el middleware)
    return render(request, 'service/service.html')