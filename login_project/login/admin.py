from django.contrib import admin

# Register your models here.
from .models import Login

class LoginAdmin(admin. ModelAdmin):
    list_display=('id','f_name','l_name','email')
    
admin.site.register(Login,LoginAdmin)
