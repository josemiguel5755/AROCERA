from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index, name="index"),
    path("dashboard" , views.dashboard, name="dashboard"),
    path("detalles" , views.detalles, name="detalles"),
    path("registrodefacturas" , views.registrodefacturas, name="registrodefacturas"),
     path('registrar-factura/', views.registrar_factura, name='registrar_factura'),
    path("gestionderepresentantes" , views.gestionderepresentantes, name="gestionderepresentantes"),
    path('get-representante/<int:id>/', views.get_representante, name='get_representante'),
    path('editar-representante/<int:id>/', views.editar_representante, name='editar_representante'),
    path('eliminar-representante/<int:id>/', views.eliminar_representante, name='eliminar_representante'),
    path("representantes" , views.representantes, name="representantes"),
    path('registrar-representante/', views.registrar_representante, name='registrar_representante'),
    path('facturas/obtener/<int:invoice_id>/', views.obtener_factura, name='obtener_factura'),
    path('facturas/editar/<int:invoice_id>/', views.editar_factura, name='editar_factura'),
    path('facturas/eliminar/<int:invoice_id>/', views.eliminar_factura, name='eliminar_factura'),
    path('facturas/pagar/<int:invoice_id>/', views.pagar_factura, name='pagar_factura'),
    
    
]