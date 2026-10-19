from django.contrib import admin;
from .models import Contato, Projeto, Contato;

# Register your models here.
admin.site.register(Projeto)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'assunto',
        'criado_em',
    )

    search_fields = (
        'nome',
        'email',
        'assunto',
    )

    list_filter = ('criado_em',)

    readonly_fields = ('criado_em',)
