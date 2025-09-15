from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UsuarioViewSet, login_view, mesero_tasks, cajero_tasks, admin_tasks

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    # Login
    path('login/', login_view, name='login'),

    # Rutas por rol
    path('mesero_tasks/', mesero_tasks, name='mesero_tasks'),
    path('cajero_tasks/', cajero_tasks, name='cajero_tasks'),
    path('admin_tasks/', admin_tasks, name='admin_tasks'),

    # API REST de usuarios
    path('', include(router.urls)),
]

"""
Definicion de endponit:

    También puede referirse a un punto de acceso específico en un servidor al que un cliente API
    se dirige para solicitar y recibir datos o funcionalidades, como una URL.
    
"""