from ast import For
import email
from xml.dom import UserDataHandler
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from user.models import *
from user.serializers import *
from datetime import date
import requests
import xmltodict
import os
import traceback

# Create your views here.


class TipoUsuarioList(generics.ListAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


class UsersList(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsuariosList(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class InstitutionList(generics.ListAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class PhoneInstitutionList(generics.ListAPIView):
    queryset = PhoneInstitution.objects.all()
    serializer_class = PhoneInstitutionSerializer
    
class PhoneUserList(generics.ListAPIView):
    queryset = PhoneUser.objects.all()
    serializer_class = PhoneUserSerializer
class VoluntaryList(generics.ListAPIView):
    queryset = Voluntary.objects.all()
    serializer_class = VoluntarySerializer

class AttendenceList(generics.ListAPIView):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
class AccountableList(generics.ListAPIView):
    queryset = Accountable.objects.all()
    serializer_class = AccountableSerializer


@api_view(['POST'])
def register(request):
    user_data = request.data
    existingUser = None
    try:
        existingUser = User.objects.get(email=user_data['email'])
    except User.DoesNotExist:
        pass
    except Exception as ex:
        print(ex)
        return Response('Error fetching existing user.')

    if existingUser != None:
        return Response({
            'status': 'email_exists'
        })

    try:
        # MUDAR ESSE IS_ACTIVE PRA FALSE DEPOIS. Isso sendo TRUE faz com que alguém consiga logar com uma conta não confirmada pelo email!!!!!!!
        new_auth_user = User.objects.create_user(
            username=user_data['email'], email=user_data['email'], password=user_data['password'], is_active=True)
    except:
        return Response({
            'status': 'error'
        })

    try:
        tipo_usuario = TipoUsuario.objects.get(
            pk=user_data['tipo_usuario'])

        new_usuario = Usuario.objects.create(
            user=new_auth_user,
            nome=user_data['nome'],
            sobrenome=user_data['sobrenome'],
            cpf=user_data['cpf'],
            tipo_usuario=tipo_usuario, 
        )
        new_usuario.hash_confirm_register = new_usuario.hash()
        new_usuario.save()

    except Exception as ex:
        print(ex)
        new_auth_user.delete()
        return Response({
            'status': 'error'
        })

    serializer = UsuarioSerializer(new_usuario)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def DesativarInscricao(request):
    userId_data = request.data
    try:
        usuario = Usuario.objects.get(pk=userId_data['id'])
        User.objects.filter(email=usuario.user).update(
            is_active=False,
        )
    except Exception as ex:
        print(ex)
        return Response({
            'status': 'error'
        })
    return Response({
        'status': 'ok'
    })


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def usuario(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)

    serializer = UsuarioSerializer(usuario)

    return JsonResponse(serializer.data, safe=False)


