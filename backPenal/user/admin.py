from django.contrib import admin
from user.models import *
# Register your models here.


admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Address)
admin.site.register(Attendence)
admin.site.register(PhoneUser)
admin.site.register(PhoneInstitution)
admin.site.register(Voluntary)
admin.site.register(Institution)

