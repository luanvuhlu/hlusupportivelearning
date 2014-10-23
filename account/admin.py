from django.contrib import admin
import hashlib
from models import CUser
import logging
log=logging.getLogger(__name__)

class CUserAdmin(admin.ModelAdmin):
    # readonly_fields = ['']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            password=form.cleaned_data['password']
            obj.password=obj.make_password(password)
            log.debug(obj.password)
        obj.save()


# Register your models here.
admin.site.register(CUser, CUserAdmin)
