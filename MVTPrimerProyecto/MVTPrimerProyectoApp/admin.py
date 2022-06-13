from django.contrib import admin
from MVTPrimerProyectoApp.models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'nacimiento')
    list_filter = ('nombre', 'edad', 'nacimiento')
    search_fields = ('nombre', 'edad', 'nacimiento')
    ordering = ('nombre', 'edad', 'nacimiento')

admin.site.register(Persona, PersonaAdmin)
