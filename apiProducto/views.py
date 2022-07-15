from urllib import request
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from productos.models import *
from productos.models import Producto as ProductoModel
from rest_framework import permissions, status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from . import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

User = get_user_model()
@csrf_exempt
@api_view(['GET', 'POST'])
def Producto(request):

    if request.method == 'GET':
        producto = ProductoModel.objects.all()
        serializer = serializers.ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def marca(request):
    if request.method == 'GET':
        marca = Marca.objects.all()
        serializer = serializers.MarcaSerializer(marca, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.MarcaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
   

@csrf_exempt
@api_view(['GET', 'POST'])
def tipo_producto(request):
    if request.method == 'GET':
        tipo_productox = Tipo_producto.objects.all()
        serializer = serializers.tipo_productoSerializer(tipo_productox, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.tipo_productoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductoViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ProductoSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre',)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            nombre = serializer.validated_data.get('nombre')
            precio = serializer.validated_data.get('precio')
            precio_costo = serializer.validated_data.get('precio_costo')
            descripcion = serializer.validated_data.get('descripcion')
            imagen = serializer.validated_data.get('imagen')
            tipo_producto = serializer.validated_data.get('tipo_producto')
            marca = serializer.validated_data.get('marca')
            return Response({"nombre": nombre, "precio": precio,})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk = None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def patrial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

        
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)