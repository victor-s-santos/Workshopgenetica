from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from ajax import views
from ajax.api.viewsets import PerguntasViewSet

router = routers.DefaultRouter()
router.register(r'ajax', PerguntasViewSet, base_name = 'Perguntas')


urlpatterns = [
	path('api/', include(router.urls)),
	path('', include('core.urls')),
	path('graficos/', include('graficos.urls')),
	path('perguntas/', include('ajax.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

