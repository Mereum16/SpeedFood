from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('registrarPedido/', views.registrarPedido, name="registrar_pedido"),
    path('edicionPedido/<codigo>', views.edicionPedido, name="editar_pedido"),
    path('editarPedido/', views.editarPedido),
    path('eliminarPedido/<codigo>', views.eliminarPedido, name="eliminar_pedido"),
    # Nuevas vistas:
    path('reporte/', views.reporte_view, name='reporte_view'),
    path('busqueda/', views.busqueda_view, name='busqueda_view'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('galeria/', views.galeria_productos, name='galeria_productos')
]