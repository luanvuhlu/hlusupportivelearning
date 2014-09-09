from django.contrib import admin
from models import Subject, SubjectYear, Document, AssignmentForm, ScheduleStudy, StudyDocument
# Register your models here.
admin.site.register(Subject)
admin.site.register(SubjectYear)
admin.site.register(Document)
admin.site.register(AssignmentForm)
admin.site.register(ScheduleStudy)
admin.site.register(StudyDocument)