from rest_framework import serializers
from apps.usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'role']

        """ 
            es un objeto que transporta datos entre capas de una aplicación,
            como el frontend y el backend, sin lógica de negocio.
        """