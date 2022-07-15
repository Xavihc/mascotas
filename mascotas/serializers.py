from productos.models import Producto,Tipo_producto
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Tipo_productoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_producto
        fields = ['nombre']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url','tipo_producto', 'nombre', 'precio', 'descripcion']        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']