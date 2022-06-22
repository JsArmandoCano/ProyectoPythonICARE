from django.urls import path
from . import views

urlpatterns = [
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('galeria/<slug:category_slug>/', views.galeria, name='photo_by_category'),
    path('eventos/', views.eventos, name='eventos'),
    path('niños/', views.niños, name='niños'),
    path('contacto/', views.contacto, name='contacto'),
]