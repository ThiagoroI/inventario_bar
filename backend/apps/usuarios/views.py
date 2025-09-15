from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from apps.usuarios.models import Usuario
from apps.usuarios.dto.usuario_dto import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    """Es un ViewSet de Django REST Framework, 
        y sirve para crear automáticamente un CRUD completo 
        (Create, Read, Update, Delete) sobre tu modelo
    """
    
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)
    return Response({'error': 'Credenciales incorrectas'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_tasks(request):
    if request.user.role != 'admin':
        return Response({"error": "No autorizado"}, status=403)
    # Retornar tareas del administrador
    return Response({
        "tasks": [
            "Gestionar usuarios",
            "Ver reportes",
            "Configurar sistema",
            "Administrar inventario",
            "Controlar mesas y pedidos",
            "Configurar roles y permisos"
        ]
    })
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mesero_tasks(request):
    if request.user.role != 'mesero':
        return Response({"error": "No autorizado"}, status=403)
    # Retornar tareas del mesero
    return Response({
        "tasks": [
            "Tomar pedidos",
            "Seleccionar mesa",
            "Buscar el producto",
            "Inventario en línea",
            "Actualizar estado de la mesa",
            "Modificar pedido"
        ]
    })
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cajero_tasks(request):
    if request.user.role != 'cajero':
        return Response({"error": "No autorizado"}, status=403)
    # Retornar tareas del cajero
    return Response({
        "tasks": [
            "Cancelar pedido",
            "Ver pedido",
            "Método de pago: Tarjeta crédito, Tarjeta débito, Efectivo"
        ]
    })    

    """
    funciones para entrar a cada uno de los roles, validaciones que envia el frontend
    """