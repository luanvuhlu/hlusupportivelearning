from django.contrib import admin
from models import FindingGroupNews, GroupMember, GroupMemberUnknown

class FindingGroupNewsAdmin(admin.ModelAdmin):
    list_display=('subject', 'date_created','public', 'deactived')
    readonly_fields=('user', )
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()
class GroupMemberAdmin(admin.ModelAdmin):
    pass
class GroupMemberUnknownAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(FindingGroupNews, FindingGroupNewsAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
admin.site.register(GroupMemberUnknown, GroupMemberUnknownAdmin)