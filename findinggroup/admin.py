from django.contrib import admin
from models import FindingGroupNews, GroupMember, GroupMemberUnknown, Subject

class FindingGroupNewsAdmin(admin.ModelAdmin):
    pass
class GroupMemberAdmin(admin.ModelAdmin):
    pass
class GroupMemberUnknownAdmin(admin.ModelAdmin):
    pass
class SubjectAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Subject, SubjectAdmin)
admin.site.register(FindingGroupNews, FindingGroupNewsAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
admin.site.register(GroupMemberUnknown, GroupMemberUnknownAdmin)