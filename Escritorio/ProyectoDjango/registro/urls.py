# urls.py

from django.urls import path
from . import views
from .views import (
    cliente_potencial_list,
    cliente_potencial_create,
    cliente_potencial_update,
    cliente_potencial_delete,
    hacer_cliente_vigente,
)

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('registro_cliente_potencial/', views.registro_cliente_potencial, name='registro_cliente_potencial'),
    path('registro_cliente_vigente/', views.registro_cliente_vigente, name='registro_cliente_vigente'),
    path('reporte_diario/', views.reporte_diario, name='reporte_diario'),
    path('cliente_potencial/', cliente_potencial_list, name='cliente_potencial_list'),
    path('cliente_potencial/nuevo/', cliente_potencial_create, name='cliente_potencial_create'),
    path('cliente_potencial/<int:pk>/editar/', cliente_potencial_update, name='cliente_potencial_update'),
    path('cliente_potencial/<int:pk>/eliminar/', cliente_potencial_delete, name='cliente_potencial_delete'),
    path('hacer_cliente_vigente/<int:pk>/', hacer_cliente_vigente, name='hacer_cliente_vigente'),
    path('cliente_vigente/', views.cliente_vigente_list, name='cliente_vigente_list'),
    path('cliente_vigente/<int:pk>/editar/', views.cliente_vigente_update, name='cliente_vigente_update'),
    path('cliente_vigente/<int:pk>/eliminar/', views.cliente_vigente_delete, name='cliente_vigente_delete'),
    path('cliente_potencial/', views.cliente_potencial_list, name='cliente_potencial_list'),
    path('casos_quejas/', views.registro_caso_cliente, name='casos_quejas'),
    
    
]
