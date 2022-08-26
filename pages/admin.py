from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'image_name',
        'category',
        'is_available',
    )
    list_filter = ('category', 'is_available')
    
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'evento_name',
        'fecha_evento',
        'is_available',
    )
    search_fields = ('evento_name', )
    list_filter = ('fecha_evento', 'is_available')
    
class AvisosAdmin(admin.ModelAdmin):
    list_display = (
        'aviso_name',
        'is_available',
    )
    
class DominicalesAdmin(admin.ModelAdmin):
    list_display = (
        'name_dom',
        'fecha',
        'dia',
        'is_available',
    )
    search_fields = ('name_dom', )
    list_filter = ('dia', 'is_available')
    
class TemasAdmin(admin.ModelAdmin):
    list_display = (
        'name_tema',
        'fecha',
        'is_available',
        'created_date',
    )
    search_fields = ('name_tema', )
    list_filter = ('fecha', 'is_available')
    
class VivoAdmin(admin.ModelAdmin):
    list_display = (
        'name_vivo',
        'is_available',
    )
    search_fields = ('name_vivo', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Avisos, AvisosAdmin)
admin.site.register(Dominicales, DominicalesAdmin)
admin.site.register(Vivo, VivoAdmin)
admin.site.register(TemasDom, TemasAdmin)