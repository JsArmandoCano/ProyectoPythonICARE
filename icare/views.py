from django.shortcuts import render
from pages.models import Avisos

def home(request):
    avisos = Avisos.objects.all().filter(is_available=True) 
    
    return render(request, 'home.html', {
        'avisos': avisos,
    })