from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def contact(request):
    # Esta sí es privada (usando el decorador o el middleware)
    return render(request, 'contact/contact.html')