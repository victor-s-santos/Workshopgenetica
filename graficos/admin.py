from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Palestrante, Pontuacao, Evento, MiniCursos, PontuacaoMinicursos



class PontuacaoResource(resources.ModelResource):
	class Meta:
		model = Pontuacao
		fields = ('palestrante__nome', 'pontuacao', 'nome', 'sugestao')
		#fields = '__all__' esse cara deixa em branco

class PontuacaoAdmin(ImportExportModelAdmin):
	resource_class = PontuacaoResource
	date_hierarchy = 'data'
	list_display = ['data', 'palestrante', 'pontuacao', 'email', 'sugestao']
	search_fields = ['palestrante', 'email', 'data']
	list_filter = ['pontuacao', 'data']

class PalestranteAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_display = ['nome', 'id', 'data']
	search_fields = ['nome']
	list_filter = ['data']

class MiniCursosAdmin(admin.ModelAdmin):
	date_hierarchy = 'data'
	list_filter = ['minicurso', 'ministrante']
	list_display = ['minicurso', 'ministrante', 'data']

class PontuacaoMinicursosResource(resources.ModelResource):
	class Meta:
		model = PontuacaoMinicursos
		fields = ('minicurso__minicurso', 'nome', 'clareza', 'tempo', 'tema', 'relevancia')

class PontuacaoMinicursosAdmin(ImportExportModelAdmin):
	resource_class = PontuacaoMinicursosResource
	date_hierarchy = 'data'
	search_fields = ['data', 'minicurso']
	list_filter = ['data', 'minicurso', 'clareza', 'tempo', 'tema', 'relevancia']
	list_display = ['minicurso', 'clareza', 'tempo', 'tema', 'relevancia', 'email', 'data']

class EventoResource(resources.ModelResource):
	class Meta:
		model = Evento
		fields = ('nome', 'limpeza', 'organizacao', 'coffe_break', 'tema', 'sugestao')

class EventoAdmin(ImportExportModelAdmin):
	resource_class = EventoResource
	date_hierarchy = 'data'
	list_filter = ['data','limpeza', 'organizacao', 'coffe_break', 'tema']
	list_display = ['nome', 'limpeza', 'organizacao', 'coffe_break', 'tema', 'data']

	
admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Pontuacao, PontuacaoAdmin)
admin.site.register(MiniCursos, MiniCursosAdmin)
admin.site.register(PontuacaoMinicursos, PontuacaoMinicursosAdmin)
admin.site.register(Evento, EventoAdmin)