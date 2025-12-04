from django.contrib import admin
from .models import Pessoa 

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular') 
    search_fields = ('nome', 'email', 'celular') 

admin.site.register(Pessoa, PessoaAdmin)