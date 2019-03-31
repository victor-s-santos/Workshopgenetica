from django.urls import path
from . import views

urlpatterns = [
	path('', views.ajax_index, name='ajax_index'),
	]
