from django.contrib import admin
from models import Course, Student, UClass, Scholastic
from tag.models import Tag
from datetime import datetime
import logging
# Register your models here.
log=logging.getLogger(__name__)
class ScholasticAdmin(admin.ModelAdmin):
    readonly_fields = ('activated', )
    def save_model(self, request, obj, form, change):
        if not form.cleaned_data['name'].strip():
            start=form.cleaned_data['start_date']
            end=form.cleaned_data['end_date']
            obj.name=str(start.year)+'-'+str(end.year)
        obj.save()
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('activated', )
    def save_model(self, request, obj, form, change):
        if not form.cleaned_data['name'].strip():
            obj.name=form.cleaned_data['code']
        obj.save()
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()

class UClassAdmin(admin.ModelAdmin):
    readonly_fields = ('activated', )
    def save_model(self, request, obj, form, change):
        if not form.cleaned_data['name'].strip():
            obj.name=form.cleaned_data['code']
        obj.save()
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('activated', )
    exclude = ('account', )
    def save_model(self, request, obj, form, change):
        obj.account=request.user
        if not form.cleaned_data['alias'].strip():
            obj.alias=obj.last_name
        obj.save()
    def delete_model(self, request, obj):
        obj.activated=False
        obj.save()
# Register site
admin.site.register(Scholastic, ScholasticAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(UClass, UClassAdmin)
