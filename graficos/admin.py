from django.contrib import admin
from .models import Palestrante, Pontuacao, Evento, MiniCursos, PontuacaoMinicursos

class PontuacaoAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_display = ['data', 'palestrante', 'pontuacao', 'email', 'sugestao']
	search_fields = ['palestrante', 'email', 'data']
	list_filter = ['pontuacao', 'data']

class PalestranteAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_display = ['nome', 'id', 'data']
	search_fields = ['nome']
	list_filter = ['data']

class PontuacaoMinicursosAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	search_fields = ['data', 'minicurso']
	list_filter = ['data', 'minicurso', 'clareza', 'tempo', 'tema', 'relevancia']
	list_display = ['minicurso', 'clareza', 'tempo', 'tema', 'relevancia', 'email', 'data']

class MiniCursosAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_filter = ['minicurso', 'ministrante']
	list_display = ['minicurso', 'ministrante', 'data']

class EventoAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_filter = ['data','limpeza', 'organizacao', 'coffe_break', 'tema']
	list_display = ['nome', 'limpeza', 'organizacao', 'coffe_break', 'tema', 'data']

	
admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Pontuacao, PontuacaoAdmin)
admin.site.register(MiniCursos, MiniCursosAdmin)
admin.site.register(PontuacaoMinicursos, PontuacaoMinicursosAdmin)
admin.site.register(Evento, EventoAdmin)