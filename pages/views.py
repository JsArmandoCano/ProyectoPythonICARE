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
    
    avisos = Avisos.objects.all().filter(is_available=True) 
    
    return render(request, 'pages/eventos.html', {
        'evento': evento,
        'avisos': avisos,
    })
    
    
def dominicales(request):
    dominicales_dom = Dominicales.objects.filter(is_available=True, dia="Domingos").order_by('-fecha')[:2]
    dominicales_jue = Dominicales.objects.filter(is_available=True, dia="Jueves").order_by('-fecha')[:2]
    dominicales_mar = Dominicales.objects.filter(is_available=True, dia="Martes").order_by('-fecha')[:2]
    
    return render(request, 'pages/dominicales.html', {
        'dominicales_dom': dominicales_dom,
        'dominicales_jue': dominicales_jue,
        'dominicales_mar': dominicales_mar,
    })
    
    
def dia(request, dia):
    if dia == "domingos":
        dia_select = Dominicales.objects.all().filter(is_available=True, dia="Domingos").order_by('-fecha')
        dia_consulta = "Domingo"
        
    elif dia == "jueves":
        dia_select = Dominicales.objects.all().filter(is_available=True, dia="Jueves").order_by('-fecha')
        dia_consulta = "Jueves"
        
    elif dia == "martes":
        dia_select = Dominicales.objects.all().filter(is_available=True, dia="Martes").order_by('-fecha')
        dia_consulta = "Martes"
        
    return render(request, 'pages/dominicales_dia.html', {
        'dia_select': dia_select,
        'dia_consulta': dia_consulta,
    })
    

def temas(request):
    tema = TemasDom.objects.all().filter(is_available=True) 
    paginator = Paginator(tema, 12)
    page = request.GET.get('page')
    page_temas = paginator.get_page(page) 
    
    return render(request, "pages/temas.html", {
        'tema': page_temas,
    })
    
    
def dev_dia(request):
    return render(request, 'pages/today.html')

    
def vivo(request):
    urlvideo = Vivo.objects.all().filter(is_available=True) 
    
    return render(request, 'pages/vivo.html', {
        'urlvideo': urlvideo,
    })
    

def niños(request):
    return render(request, 'pages/niños.html')
    

def contacto(request):
    return render(request, 'pages/contacto.html')