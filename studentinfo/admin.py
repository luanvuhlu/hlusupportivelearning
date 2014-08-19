from django.contrib import admin
from models import Course, Speciality, Student, UClass
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    pass
class SpecialityAdmin(admin.ModelAdmin):
    pass
class StudentAdmin(admin.ModelAdmin):
    pass
class UClassAdmin(admin.ModelAdmin):
    pass

# Register site
admin.site.register(Course, CourseAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(UClass, UClassAdmin)
