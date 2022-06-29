from audioop import reverse
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from tkinter import image_names
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'category'   
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('photo_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
    
    
class Photo(models.Model):
    image_name = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='photos/fotos')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    
class Evento(models.Model):
    evento_name = models.CharField(max_length=50)
    evento_image = models.ImageField(upload_to='photos/fotos')
    description_1 = models.CharField(max_length=100)
    description_2 = models.TextField()
    fecha_evento = models.DateField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.evento_name
    
    
class Dominicales(models.Model):
    CHOICES = (
        ('Domingos', 'Domingos'),
        ('Jueves', 'Jueves'),
        ('Martes', 'Martes'),
    )
    
    name_dom = models.CharField(max_length=100, blank=False)
    fecha = models.DateField()
    dia = models.CharField(choices=CHOICES, max_length=50, default='Domingo')
    evento_image = models.ImageField(upload_to='photos/fotos', blank=False)
    pdf = models.FileField(upload_to='pdf/pdfs', blank=False)
    audio = models.FileField(upload_to='audio/audios', blank=False)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_dom
    
    
class Vivo(models.Model):
    name_vivo = models.CharField(max_length=200)
    frame = models.URLField(max_length=200)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_vivo