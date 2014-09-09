from django.db import models
from django.utils import timezone
from studentinfo.models import Student
from document.models import Subject
PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
CLASS_TYPE=(('Theory', 'T'), ('Seminar', 'S'))
HOURS=(('1,2', '1,2'), ('3,4', '3,4'), ('5,6', '5,6'), ('7,8', '7,8'), ('9,10', '9,10'), ('11,12', '11,12'), ('13,14,15', '13,14,15'))
DAYS_OF_WWEK=()
# Create your models here.
class TimeTable(models.Model):
	student=models.ForeignKey(Student)
	year=models.CharField(max_length=4, blank=True)
	semester=models.CharField(max_length=2, blank=True)
	created_time=models.DateTimeField(default=timezone.now(), blank=False)
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return self.student.__str__()
class SubjectClass(models.Model):
	subject=models.ForeignKey(Subject)
	timeTable=models.ForeignKey(TimeTable)
	theory_class=models.CharField(max_length=5, blank=False)
	seminar_class=models.CharField(max_length=5, blank=True)
	start_date=models.DateTimeField(blank=False)
	end_date=models.DateTimeField(blank=False)
	def __unicode__(self):
		return self.subject.__str__()
class SubjectStudyDay(models.Model):
	subject_class=models.ForeignKey(SubjectClass)
	day_name=models.CharField(max_length=10, blank=False)
	day_hours=models.CharField(max_length=10, blank=False, choices=HOURS)
	day_location=models.CharField(max_length=10, blank=False)
	class_type=models.CharField(max_length=2, blank=False, choices=CLASS_TYPE)