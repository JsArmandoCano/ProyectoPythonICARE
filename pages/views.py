from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def nosotros(request):
    return render(request, 'pages/nosotros.html')

def galeria(request, category_slug=None):
    links = Category.objects.all()
    
    categories = None
    fotos = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        fotos = Photo.objects.filter(category=categories, is_available=True)
        paginator = Paginator(fotos, 16)
        page = request.GET.get('page')
        page_fotos = paginator.get_page(page)
        fotos_count = fotos.count()
        
    else: 
        fotos = Photo.objects.all().filter(is_available=True)
        paginator = Paginator(fotos, 16)
        page = request.GET.get('page')
        page_fotos = paginator.get_page(page)
        fotos_count = fotos.count()
    
    return render(request, 'pages/galeria.html', {
        'links': links,
        'fotos': page_fotos,
        'fotos_count': fotos_count,
    })


def eventos(request):
    evento = Evento.objects.all().filter(is_available=True) 
    
    return render(request, 'pages/eventos.html', {
        'evento': evento,
    })
    

def contacto(request):
    return render(request, 'pages/contacto.html')