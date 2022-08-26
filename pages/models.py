from email.policy import default
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField('Nombre de la Categoria:', max_length=50, unique=True)
    description = models.CharField('Descripción:', max_length=255, blank=True)
    slug = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'   
        verbose_name_plural = 'Categorias'
        
    def get_url(self):
        return reverse('photo_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
    
    
class Photo(models.Model):
    image_name = models.CharField('Nombre de la Imagen:', max_length=20, blank=True)
    image = models.ImageField('Imagen:', upload_to='photos/fotos')
    is_available = models.BooleanField('Activo?', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Foto'   
        verbose_name_plural = 'Fotos'
    
    def __str__(self):
        return self.image_name
    
    
class Evento(models.Model):
    evento_name = models.CharField('Nombre del Evento:', max_length=50)
    evento_image = models.ImageField('Imagen:', upload_to='photos/fotos')
    description_1 = models.CharField('Descripción 1:', max_length=100)
    description_2 = models.TextField('Descripción 2:')
    fecha_evento = models.DateField('Fecha del Evento:')
    is_available = models.BooleanField('Activo?',default=True)
    
    class Meta:
        verbose_name = 'Evento'   
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.evento_name
    
    
class Avisos(models.Model):
    aviso_name = models.CharField('Nombre del Aviso:', max_length=50)
    aviso_image = models.ImageField('Imagen:', upload_to='photos/fotos')
    is_available = models.BooleanField('Activo?', default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Aviso'   
        verbose_name_plural = 'Avisos'
    
    def __str__(self):
        return self.aviso_name
    
    
class Dominicales(models.Model):
    CHOICES = (
        ('Domingos', 'Domingos'),
        ('Jueves', 'Jueves'),
        ('Martes', 'Martes'),
    )
    
    name_dom = models.CharField('Título Dominical:', max_length=100, blank=False)
    fecha = models.DateField('Fecha:')
    dia = models.CharField('Dia:', choices=CHOICES, max_length=50, default='Domingo')
    evento_image = models.ImageField('Imagen:', upload_to='photos/fotos', blank=False)
    pdf = models.FileField('Pdf:', upload_to='pdf/pdfs', blank=False)
    audio = models.FileField('Audio:', upload_to='audio/audios', blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name = 'Dominical'   
        verbose_name_plural = 'Dominicales'
    
    def __str__(self):
        return self.name_dom
    

class TemasDom(models.Model):
    name_tema = models.CharField('Tema', max_length=60, blank=False)
    tema_image = models.ImageField('Imagen:', upload_to='photos/fotos', blank=False, default=None)
    fecha = models.DateField('Fecha:')
    pdf = models.FileField('Pdf:', upload_to='pdf/pdfs', blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tema'   
        verbose_name_plural = 'Temas'
    
    def __str__(self):
        return self.name_tema
    
    
class Vivo(models.Model):
    name_vivo = models.CharField('Nombre:',max_length=200)
    frame = models.URLField('URL:',max_length=200)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'En vivo'   
        verbose_name_plural = 'En vivos'
    
    def __str__(self):
        return self.name_vivo