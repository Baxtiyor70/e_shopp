from django.contrib import admin

from .models import CustomUser,CodeConfirmation

@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','gender','username','age']

    class Meta:
         model = CustomUser

@admin.register(CodeConfirmation)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'code', 'code_token']