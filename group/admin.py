from django.contrib import admin
from models import Group, GroupMember

class GroupAdmin(admin.ModelAdmin):
    list_display=('subject', 'created_time','public', 'activated')
    readonly_fields=('user', )
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()
class GroupMemberAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()

# Register your models here.
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)