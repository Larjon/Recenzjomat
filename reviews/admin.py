from django.contrib import admin
from .models import Ksiazka, Recenzja, Kategoria

admin.site.register(Ksiazka)
admin.site.register(Recenzja)
admin.site.register(Kategoria)

class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'autor', 'kategorie')