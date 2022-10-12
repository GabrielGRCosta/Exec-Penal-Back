from user.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ['id', 'tipo']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']


class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Usuario
        fields = ['id', 'user', 'nome', 'sobrenome', 'cpf', 'tipo_usuario']
        depth = 1

