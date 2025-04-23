from django.contrib import admin
from django.urls import path
from projetos.views import listar_projetos  # importa a função que mostra os projetos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                     # URL do painel admin
    path('', listar_projetos, name='listar_projetos'),   # página inicial do site
]

# Mostra as imagens no navegador durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



