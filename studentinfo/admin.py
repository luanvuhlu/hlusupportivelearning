from django.contrib import admin
from models import Course, Speciality, Student, UClass
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()
class SpecialityAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()
class StudentAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()
class UClassAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()

# Register site
admin.site.register(Course, CourseAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(UClass, UClassAdmin)
