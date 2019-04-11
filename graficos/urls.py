from django.urls import path
from . import views

urlpatterns = [
	path('', views.grafico_index, name='grafico_index'),
	path('grafico_palestrantes', views.grafico_palestrantes, name='grafico_palestrantes'),
	path('grafico_geral/', views.grafico_geral, name='grafico_geral'),
	path('grafico_minicurso/', views.grafico_minicurso, name='grafico_minicurso'),
	path('avalia/', views.avalia, name='avaliacao'),
	path('avalia_evento/', views.avalia_evento, name='avalia_evento'),
	path('avalia_minicurso/', views.avalia_minicurso, name='avalia_minicurso'),
	]
