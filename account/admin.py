from django.contrib import admin
from models import CUser

class CUserAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(CUser, CUserAdmin)