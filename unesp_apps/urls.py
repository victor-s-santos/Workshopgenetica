from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ajax import views

urlpatterns = [
	path('api/', views.Get_Perguntas_List.as_view()),
	path('', include('core.urls')),
	path('graficos/', include('graficos.urls')),
	path('perguntas/', include('ajax.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

