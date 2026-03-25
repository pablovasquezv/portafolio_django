from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def testimonials(request):
    # Esta sí es privada (usando el decorador o el middleware)
    return render(request, 'testimonial/testimonials.html')