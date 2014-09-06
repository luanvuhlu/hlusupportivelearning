from django.db import models
from django.utils import timezone
from studentinfo.models import Course, Speciality

# Create your models here.
PUBLIC_YN=(('Y', 'Y', ('N', 'N')))
YN=(('Y', 'Y', ('N', 'N')))
SEMESTER=(('1', '1'), ('2', '2'))
ASSIGNMENT_TYPE=(('Person', 'P'), ('Group', 'G'), ('Final', 'F'))
ASSIGNMENT_METHOD=(('Print', 'P'), ('Hand', 'H'))
SCHEDULE_STUDY_TYPE=(('Theory', 'T'), ('Seminar', 'S'))
STUDY_DOCUMENT_TYPE=(('Book', 'B'), ('Law', 'L'), ('Website', 'W'))
class Subject(models.Model):
    subject_code=models.CharField(max_length=20, blank=False)
    subject_name=models.CharField(max_length=100,blank=False)
    subject_short_name=models.CharField(max_length=30, blank=True)
    created_time=models.DateTime(default=timezone.now(), blank=False)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
    course_credit=models.SmallInteger(default=2, blank=False)
    speciality=models.CharField(max_length=10, blank=True)
    description=models.CharField(max_length=200)
    deactived=models.BooleanField(default=False)
    def __unicode__(self):
        if self.subject_short_name:
            return self.subject_short_name
        return self.subject_code
class SubjectYear(models.Model):
	subject=models.ForeignKey(Subject)
	course=models.ForeignKey(Course)
	speciality=models.CharField(max_length=10, blank=True)
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return subject.__str__()+course.__str__()
class Document(models.Model):
	subject=models.ForeignKey(Subject)
	speciality=models.ForeignKey(Speciality)
	semester=models.CharField(max_length=2, blank=True, choices=SEMESTER)
	course=models.CharField(max_length=20, blank=True)
	year=models.CharField(max_length=4, blank=True)
	final_exam=models.CharField(max_length=100, blank=True)
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return subject.__str__()
class AssignmentForm(models.Model):
	document=models.ForeignKey(Document)
	type=models.CharField(max_length=2, blank=False, choices=ASSIGNMENT_TYPE)
	method=models.CharField(max_length=1, blank=False, choices=ASSIGNMENT_METHOD)
	max_page=models.SmallInteger(blank=True)
	year=models.DateTime(default=timezone.now())
	note=models.CharField(max_length=45, blank=True)
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return document.__str__()
class ScheduleStudy(models.Model):
	type=models.CharField(max_length=1, choices=SCHEDULE_STUDY_TYPE, blank=False)
	order_type=models.SmallInteger()
	order=models.SmallInteger()
	requirement=models.CharField(max_length=200, blank=True)
	study_content=models.CharField(max_length=200, blank=True)
	assignment=models.CharField(max_length=45, blank=True)
	note=models.CharField(max_length=45, blank=True)
	year=models.DateTime(default=timezone.now())
	deactived=models.BooleanField(default=False)
class StudyDocument(models.Model):
	document=models.ForeignKey(Document)
	name=models.CharField(max_length=100, blank=False)
	type-models.CharField(max_length=2, choices=STUDY_DOCUMENT_TYPE, blank=False)
	compulsory=models.CharField(max_length=1, choices=YN, blank=False)
	year=models.DateTime(timezone.now())
	deactived=models.BooleanField(default=False)
		
		