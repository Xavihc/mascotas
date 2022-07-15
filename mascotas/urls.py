from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from mascotas import views



urlpatterns = [
    
    path('', views.index, name='index'),
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('api/', include('apiProducto.urls')),
    path('agregarc/<int:producto_id>', views.agregarAlCarro, name='add'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)