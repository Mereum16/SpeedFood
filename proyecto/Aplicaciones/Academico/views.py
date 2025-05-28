from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from django.contrib import messages
from .models import Producto


# Create your views here.


def home(request):
    pedidosListados = Pedido.objects.all()
    productos = Producto.objects.all()  # Carga todos los productos
    messages.success(request, '¡Pedidos Listados!')
    return render(request, "gestionPedidos.html", {
        "pedidos": pedidosListados,
        "productos_home": productos  # Enviado al base.html
    })


def registrarPedido(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']

        # Validar si el código ya existe
        if Pedido.objects.filter(codigo=codigo).exists():
            messages.error(request, f"El código '{codigo}' ya está registrado. Por favor usa otro código.")
            return redirect('registrar_pedido')  # Cambia aquí si tienes otra URL para el formulario

        pedido = Pedido.objects.create(
            codigo=codigo, nombre=nombre, creditos=creditos)
        messages.success(request, '¡Pedido registrado!')
        return redirect('/')

    # Si no es POST, simplemente redirigir o mostrar el formulario
    return redirect('registrar_pedido')


def edicionPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    return render(request, "edicionPedido.html", {"pedido": pedido})


def editarPedido(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    pedido = Pedido.objects.get(codigo=codigo)
    pedido.nombre = nombre
    pedido.creditos = creditos
    pedido.save()

    messages.success(request, '¡Pedido Actualizado!')

    return redirect('/')


def eliminarPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    pedido.delete()

    messages.success(request, '¡Pedido Eliminado!')

    return redirect('/')

from django.db.models import Q

def busqueda_view(request):
    query = request.GET.get("q")
    resultados = Pedido.objects.filter(
        Q(nombre__icontains=query) | Q(codigo__icontains=query)
    ) if query else []

    return render(request, "busqueda.html", {"resultados": resultados, "query": query})


def reporte_view(request):
    pedidos = Pedido.objects.all().order_by('codigo')
    codigo_filter = request.GET.get('creditos')

    if codigo_filter:
        pedidos = pedidos.filter(codigo=codigo_filter)

    return render(request, "reporte.html", {"pedidos": pedidos, "codigo_filter": codigo_filter})


def galeria_productos(request):
    productos = Producto.objects.all()
    return render(request, 'galeriaProductos.html', {'productos': productos})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('home')