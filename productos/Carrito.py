class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]

        else:
            self.carrito = carrito

    def agregarProducto(self, Producto, cantidad):
        id = str(Producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": Producto.id,
                "nombre": Producto.nombre,
                "precio": Producto.precio,
                "cantidad": cantidad,
                "subtotal": cantidad * Producto.precio
            }
        else: 
            self.carrito[id]["cantidad"] += cantidad
            self.carrito[id]["subtotal"] += cantidad*Producto.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminarProducto(self, Producto):
        id = str(Producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def limpiarCarrito(self):
        self.session["carrito"] = {}
        self.session.modified = True