from xml.etree.ElementInclude import include
from django.urls import path
from apiProducto import views
from mascotas import views
from . import views
from django.contrib import admin

app_name= 'productos'
urlpatterns = [

    path('mostrar_productos',views.mostrar_productos,name='mostrar_productos'),
    path('', views.index, name='index'),
    path('mostrado/<id>/',views.mostrado,name='mostrado'),
    path('pago/<id>/',views.pago,name='pago'),
    path('administracion',views.administracion,name='administracion'),
    path('modificar/<id>/',views.modificar,name='modificar'),
    path('eliminar/<id>/',views.eliminar,name='eliminar'),
    path('modificar_producto',views.modificar_producto,name='modificar_producto'),
    path('agregar_producto',views.agregar_producto,name='agregar_producto'),
    path('agregar',views.agregar,name='agregar'),
    path('frm_iniciar_sesion',views.frm_iniciar_sesion,name='frm_iniciar_sesion'),
    path('iniciar_sesion',views.iniciar_sesion,name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('agregarc/<int:producto_id>', views.agregarAlCarro, name='add'),
    path('donacion/', views.donacion, name='donacion'),
    #path('contacto/', views.contacto, name='contacto'),
    #path('nosotros/',views.nosotros,name='nosotros'),
    #path('api/', include('apiProducto.urls')),
    
]
