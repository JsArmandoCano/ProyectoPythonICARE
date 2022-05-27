from unicodedata import category
from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo)
admin.site.register(Evento)