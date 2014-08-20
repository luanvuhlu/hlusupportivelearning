from django.contrib import admin
from models import CUser, Manager

class CUserAdmin(admin.ModelAdmin):
    pass
class ManagerAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(CUser, CUserAdmin)
admin.site.register(Manager, ManagerAdmin)