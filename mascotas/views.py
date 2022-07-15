from productos.models import Producto,Tipo_producto
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from productos import Carrito
from django.contrib.auth import get_user_model

User = get_user_model()
     

def index(request):
    listado_clientes =Producto.objects.all()
    clientes ={'listado_clientes':listado_clientes }
    return render(request, 'productos/index.html',clientes)

def registro(request):
    if request.method =="POST":
        nombre = request.POST["username"]
        correo = request.POST["email"]
        clave = request.POST["password"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))

        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'producto/registro.html')

def agregarAlCarro(request, producto_id):
    cantidad = request.POST["cantidad"].strip()
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregarProducto(producto, cantidad)

    return redirect(f'productos:agregarc/{producto}')

def eliminarDelCarro(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminarProducto(producto)
    return redirect(f'productos:elimin/{producto}')

def limpiarCarro(request):
    carrito = Carrito(request)
    carrito.limpiarCarrito()
    return redirect("productos:index")