from django.db import models
from django.contrib.auth.models import User, Group
import hashlib

# Create your models here.
##########################################################
# Models de cadastro do usuário
##########################################################


class Address(models.Model):
    street = models.CharField('Rua', max_length=100, default='')
    number = models.IntegerField('Numero', default=0)
    district = models.CharField('Bairro', max_length=50, default='')
    city = models.CharField('Cidade', max_length=50, default='')
    zip = models.CharField('CEP', max_length=20, default='')
    state = models.CharField('Estado', max_length=50, default='')
    lat = models.CharField('Latitude', max_length=20, default='')
    long = models.CharField('Longitude', max_length=20, default='')

    class Meta:
        verbose_name_plural = 'Addresses'
        unique_together = ['lat', 'long']

    def __str__(self):
        return '{}-{}'.format(self.street, self.zip)

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
    escolaridade = models.CharField(max_length=45, null=True, blank=False)

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


class PhoneUser(models.Model):
    number = models.CharField('Numero', max_length=15, unique=True)
    is_active = models.BooleanField('Ativo?', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Users Phones'

    def __str__(self):
        return self.number


class Institution(models.Model):
    name = models.CharField('Nome', max_length=100, default='')
    email = models.CharField('Email', max_length=100, default='')
    address = models.OneToOneField(verbose_name='Endereco', to=Address, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = [['name', 'email'], ['name', 'address'], ['email', 'address']]

    def __str__(self):
        return self.name


class PhoneInstitution(models.Model):
    number = models.CharField('Numero', max_length=15, unique=True)
    is_active = models.BooleanField('Ativo?', default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Institutions Phones'

    def __str__(self):
        return self.number


class Voluntary(models.Model):
    # One-to-One with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # One-to-many institution-Voluntary
    institution = models.OneToOneField(Institution, on_delete=models.CASCADE, null=True)

    time_penalty = models.IntegerField(default=0)
    completed_hours = models.IntegerField(default=0)
    comments = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name_plural = 'Voluntaries'
        unique_together = ['user', 'institution']


class Accountable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        unique_together = ['user', 'institution']


class Attendence(models.Model):
    voluntary = models.OneToOneField(Voluntary, on_delete=models.CASCADE, null=True)
    institution = models.OneToOneField(Institution, on_delete=models.CASCADE, null=True)
    input_time = models.DateTimeField(auto_now_add=True)
    input_photo = models.ImageField(null=True, blank=True)
    output_time = models.DateTimeField(auto_now_add=True)
    output_photo = models.ImageField(null=True, blank=True)
    is_checked = models.BooleanField()
    # TODO: Adicionar alguma biblioteca para trabalhar com latitude e longitude
    latitude = models.CharField(max_length=15, null=True)
    longitude = models.CharField(max_length=15, null=True)
    commments = models.TextField(max_length=200, blank=True)

    class Meta:
        unique_together = ['voluntary', 'input_time', 'output_time']




