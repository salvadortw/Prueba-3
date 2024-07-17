# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('registro_cliente_potencial/', views.registro_cliente_potencial, name='registro_cliente_potencial'),
    path('registro_cliente_vigente/', views.registro_cliente_vigente, name='registro_cliente_vigente'),
    path('reporte_diario/', views.reporte_diario, name='reporte_diario'),
    path('cliente_vigente/', views.cliente_vigente_list, name='cliente_vigente_list'),
    path('cliente_vigente/<int:pk>/editar/', views.cliente_vigente_update, name='cliente_vigente_update'),
    path('cliente_vigente/<int:pk>/eliminar/', views.cliente_vigente_delete, name='cliente_vigente_delete'),
    path('cliente_potencial/', views.cliente_potencial_list, name='cliente_potencial_list'),
    path('casos_quejas/', views.registro_caso_cliente, name='casos_quejas'),
    path('agentes/', views.lista_agentes, name='lista_agentes'),
    path('agente/crear/', views.crear_agente, name='crear_agente'),
    path('agente/editar/<int:pk>/', views.editar_agente, name='editar_agente'),
    path('agente/eliminar/<int:pk>/', views.eliminar_agente, name='eliminar_agente'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('dashboard/', views.dashboard_agente, name='dashboard_agente')
    
]
