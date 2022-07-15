from productos.models import Tipo_producto, Marca, Producto, Usuario
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from apiProducto.models import UserProfileManager
from django.conf import settings
from django.shortcuts import redirect
from . import Carrito
from django.contrib.auth import get_user_model

User = get_user_model()


def registro(request):
    if request.method =="POST":
        nombre = request.POST["name"]
        correo = request.POST["email"]
        clave = request.POST["password"]
        rut = request.POST["rut"]
        User = Usuario(name = name,  rut = rut,  email = email,  password = password)
        UserProfileManager.create_user(request, email = email, name = name, password = password)
        
        User.save()

        return HttpResponseRedirect(reverse('productos:index'))
    return render(request, 'productos/registro.html')

def index(request):
    listado_clientes = Producto.objects.all()
    clientes ={'listado_clientes':listado_clientes }
    return render(request, 'productos/index.html',clientes)

def mostrar_productos(request):

    if request.POST['Buscar']:
        buscado= request.POST['Buscar']
        producto = Producto.objects.filter(nombre__icontains=buscado)
        return render(request,'productos/mostrar_productos.html',{"producto":producto,"query":buscado})
    else:
        return HttpResponse("No has introducido nada")


def mostrado(request,id):
    producto= Producto.objects.get(pk=id)

    return render(request,'productos/mostrado.html',{'producto':producto})

def pago(request,id):
    producto= Producto.objects.get(pk=id)
    user = request.user
    return render(request,'productos/pago.html',{'producto':producto, "user": user})


def administracion(request):
    listado_clientes =Producto.objects.all()
    clientes ={'listado_clientes':listado_clientes }
    return render(request, 'productos/administracion.html',clientes)


def modificar(request,id):
    producto= Producto.objects.get(pk=id)
    tipo_producto= Tipo_producto.objects.all()
    marca= Marca.objects.all()
    marca_p = producto.marca
    producto_t=producto.tipo_producto
    return render(request,'productos/modificar.html',{'producto':producto,'tipo_producto':tipo_producto,'producto_t':producto_t, 'marca':marca, 'marca_p':marca_p })


def modificar_producto(request):
    id_producto=request.POST['id_producto']
    Nombre_p=request.POST['Nombre'].strip()
    precio_p=request.POST['precio'].strip()
    precio_costo_p=request.POST['preciocosto'].strip()
    marca_p=request.POST['marcas']
    descripcion_p=request.POST['descripcion'].strip()
    imagen_p=request.FILES.get('imagen')
    tipoproducto_p=request.POST['tipoproducto']
    
    tipo=Tipo_producto.objects.get(id=tipoproducto_p)
    marcax=Marca.objects.get(id=marca_p)
    producto= Producto(id=id_producto, nombre=Nombre_p,
    precio=precio_p, precio_costo=precio_costo_p, marca=marcax, descripcion=descripcion_p, imagen =imagen_p,
    tipo_producto= tipo)

    producto.save()
    return HttpResponseRedirect(reverse('productos:administracion'))


def eliminar(request,id):
    producto= Producto.objects.get(pk=id)
    producto.delete()
    return HttpResponseRedirect(reverse('productos:administracion'))

def agregar_producto(request):
    tipo_producto= Tipo_producto.objects.all()
    marca = Marca.objects.all()
    return render(request,'productos/agregar_producto.html',{'tipo_producto':tipo_producto, 'marca': marca})

def agregar(request):
    Nombre_p=request.POST['Nombre'].strip()
    precio_p=request.POST['precio'].strip()
    precioc_p=request.POST['preciocosto'].strip()
    marca_p=request.POST['marcas']
    descripcion_p=request.POST['descripcion'].strip()
    imagen_p=request.FILES.get('imagen')
    tipoproducto_p=request.POST['tipoproducto']
    
    tipo=Tipo_producto.objects.get(id=tipoproducto_p)
    id_marca=Marca.objects.get(id=marca_p)

    producto= Producto(nombre=Nombre_p,
    precio=precio_p, precio_costo=precioc_p, marca=id_marca, descripcion=descripcion_p, imagen=imagen_p,
    tipo_producto= tipo)

    producto.save()
    return HttpResponseRedirect(reverse('productos:administracion'))

def frm_iniciar_sesion(request):
    return render(request,'productos/frm_iniciar_sesion.html')

def iniciar_sesion(request):
   email = request.POST["email"]
   clave = request.POST["clave"]    
   user = authenticate (request, email = email, password = clave)
   if user is not None:
       login(request,user)
       return HttpResponseRedirect(reverse('productos:index'))
   else:
       return HttpResponse("Usuario no registrado o no existente")     

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

def donacion(request):
    mensaje = "Gracias por donar a mascotas"
    user = request.user

    return render(request,'productos/donacion.html', {"user": request.user, "mensaje": mensaje})