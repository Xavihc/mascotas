from django.db import router
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import Producto, marca, tipo_producto

router = DefaultRouter()
router.register('producto-viewset', views.ProductoViewSet, basename='producto-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('apiProducto', Producto, name="apiProducto"),
    path('apiMarca', marca, name="apiMarca"),
    path('apiTP', tipo_producto, name="apiTP"),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]