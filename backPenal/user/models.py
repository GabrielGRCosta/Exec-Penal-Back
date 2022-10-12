from django.db import models
from django.contrib.auth.models import User, Group
import hashlib

# Create your models here.
##########################################################
# Models de cadastro do usuário
##########################################################


class TipoUsuario(models.Model):
    def __str__(self):
        return self.tipo

    tipo = models.CharField(max_length=25, null=False, blank=False)



class Usuario(models.Model):
    def __str__(self):
        return self.nome
        
    # OBS: O email e senha do usuário fica na tabela auth_user
    # Chave estrangeira da tabela auth_user padrão do django related_name='usuario'
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default='', null=False, blank=False)

    # Dados de indentificação
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)

    #identificação de usuario
    tipo_usuario = models.ForeignKey(
        TipoUsuario, on_delete=models.PROTECT, null=False, blank=False)

    

    # Campos para troca de senha e confirmação de inscrição
    hash_confirm_register = models.CharField(
        max_length=128, null=True, blank=True, default="")
    hash_confirm_senha = models.CharField(
        max_length=128, null=True, blank=True, default="")

    def hash(self):
        # Gerando hash
        return hashlib.sha512((self.nome + self.user.email).encode('utf-8')).hexdigest()


