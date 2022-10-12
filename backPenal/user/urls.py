from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    ################################ Usuario ################################
    # lista todos os usuários
    path('users/', views.UsersList.as_view(), name='list-users'),
    # lista todos os usuários 
    path('usuarios/', views.UsuariosList.as_view(), name='list-usuarios'),
    # retorna as informações de um usuário para a aba user
    path('usuario/', views.usuario, name='usuario'),

    ################################ Inscrição ################################
    # registra um usuário novo
    path('register/', views.register, name='register'),
    # lista os possíveis tipos de inscricao
    path('tipoUsuario/', views.TipoUsuarioList.as_view(),
         name='list-tipoinscricao'),
    # confirma o registro do usuário
    path('desativarInscricao/', views.DesativarInscricao,
         name='DesativarInscricao'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
