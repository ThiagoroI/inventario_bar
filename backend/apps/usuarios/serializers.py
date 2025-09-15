# usuarios/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Usuario.
    Devuelve id, username, email y role.
    """
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'role']

class LoginSerializer(serializers.Serializer):
    """
    Serializer para login. Solo recibe username y password.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
