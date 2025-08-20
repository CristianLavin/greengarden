from django.urls import path
from . import views
from paginaweb.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, registro_view, login_view

urlpatterns = [
    path('index.html', views.index),
    path('plantas.html', views.plantas),
    path('login.html', views.login, name='login'),  # Correct URL name
    path('registro.html', views.registro),
    path('maceteros.html', views.maceteros),
    path('confirmacion.html', views.confirmacion),
    path('index2.html', views.index2, name='index2'),
    path('plantas2.html', views.plantas2),
    path('maceteros2.html', views.maceteros2),
    path('despacho.html', views.despacho),
    path('confirmacion2.html', views.confirmacion2),
    path('confirmacion3.html', views.confirmacion3),
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('carrito.html', views.carrito, name="Carrito"),
    path('registro1', registro_view, name='registro_view'),  # Correct URL name
    path('logueo', login_view, name='login_view'),  # Correct URL name
]
