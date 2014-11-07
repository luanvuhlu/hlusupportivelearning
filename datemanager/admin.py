from django.contrib import admin
from models import Holiday
# Register your models here.
class HolidayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Holiday)