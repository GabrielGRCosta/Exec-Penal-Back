from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views
from rest_framework.authtoken import views as auth_views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='Exec API',
        default_version='1.0.0',
        description='API documentation of App'
    ),
    public=True
)

urlpatterns = [
    ################################ Usuario ################################
    # lista todos os usuários
    path('users/', views.UsersList.as_view(), name='list-users'),
    # lista todos os usuários 
    path('usuarios/', views.UsuariosList.as_view(), name='list-usuarios'),
    # retorna as informações de um usuário para a aba user
    path('usuario/', views.usuario, name='usuario'),

    path('api-token-auth/', auth_views.obtain_auth_token),

    ################################ Inscrição ################################
    # registra um usuário novo
    path('register/', views.register, name='register'),
    # lista os possíveis tipos de inscricao
    path('tipoUsuario/', views.TipoUsuarioList.as_view(),
         name='list-tipoinscricao'),
    # confirma o registro do usuário
    path('desativarInscricao/', views.DesativarInscricao,name='DesativarInscricao'),

    path('accountables/', views.AccountableList.as_view(), name='list-accountables'),

    path('addresses/', views.AddressList.as_view(), name='list-addresses'),

    path('attendences/', views.AttendenceList.as_view(), name='list-attendences'),

    path('institutions/', views.InstitutionList.as_view(), name='list-institutions'),

    path('phones/users/', views.PhoneUserList.as_view(), name='list-phonesusers'),

    path('phones/institutions/', views.PhoneInstitutionList.as_view(), name='list-phonesinstitutions'),

    path('voluntaries/', views.VoluntaryList.as_view(), name='list-voluntaries'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
