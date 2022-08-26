from django.urls import path
from . import views

urlpatterns = [
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('galeria/<slug:category_slug>/', views.galeria, name='photo_by_category'),
    path('eventos/', views.eventos, name='eventos'),
    path('dominicales/', views.dominicales, name='dominicales'),
    path('dominicales/<str:dia>/', views.dia),
    path('temas/', views.temas, name='tema'),
    path('devocional/', views.dev_dia, name='devocional'),
    path('vivo/', views.vivo, name='vivo'),
    path('niños/', views.niños, name='niños'),
    path('contacto/', views.contacto, name='contacto'),
]