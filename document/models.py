from django.db import models
from django.utils import timezone
from student.models import Course

# Create your models here.
PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
SEMESTER=(('1', '1'), ('2', '2'))
ASSIGNMENT_TYPE=(('P', 'Person'), ('G', 'Group'), ('F', 'Final'))
ASSIGNMENT_METHOD=(('P', 'Print'), ('H', 'Hand'))
SCHEDULE_STUDY_TYPE=(('T', 'Theory'), ('S', 'Seminar'))
STUDY_DOCUMENT_TYPE=(('B', 'Book'), ('L', 'Law'), ('W', 'Website'))
class Subject(models.Model):
    subject_code=models.CharField(max_length=20, blank=False)
    subject_name=models.CharField(max_length=100,blank=False)
    subject_short_name=models.CharField(max_length=30, blank=True)
    created_time=models.DateTimeField(default=timezone.now(), blank=False)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
    course_credit=models.SmallIntegerField(default=2, blank=False)
    speciality=models.CharField(max_length=10, blank=True)
    description=models.CharField(max_length=200, blank=True)
    activated=models.BooleanField(default=True)
    def __unicode__(self):
        if self.subject_short_name:
            return self.subject_short_name
        return self.subject_code
    def get_name(self):
        if self.subject_short_name:
            return self.subject_short_name
        return self.subject_name
class SubjectYear(models.Model):
	subject=models.ForeignKey(Subject)
	course=models.CharField(max_length=10, blank=True)
	speciality=models.CharField(max_length=10, blank=True)
	year=models.CharField(max_length=4, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.subject.__str__()
class Document(models.Model):
	subject=models.ForeignKey(Subject)
	semester=models.CharField(max_length=2, blank=True, choices=SEMESTER)
	course=models.CharField(max_length=20, blank=True)
	year=models.CharField(max_length=4, blank=True)
	final_exam=models.CharField(max_length=100, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.subject.__str__()
class AssignmentForm(models.Model):
	document=models.ForeignKey(Document)
	type=models.CharField(max_length=2, blank=False, choices=ASSIGNMENT_TYPE)
	method=models.CharField(max_length=1, blank=False, choices=ASSIGNMENT_METHOD)
	max_page=models.SmallIntegerField(blank=True, default=-1)
	year=models.CharField(max_length=4, blank=True)
	note=models.CharField(max_length=45, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.document.__str__()
class ScheduleStudy(models.Model):
	document=models.ForeignKey(Document)
	type=models.CharField(max_length=1, choices=SCHEDULE_STUDY_TYPE, blank=False)
	order_type=models.SmallIntegerField()
	order=models.SmallIntegerField()
	requirement=models.CharField(max_length=200, blank=True)
	study_content=models.CharField(max_length=200, blank=True)
	assignment=models.CharField(max_length=45, blank=True)
	note=models.CharField(max_length=45, blank=True)
	year=models.CharField(max_length=4, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.document.__str__()
class StudyDocument(models.Model):
	document=models.ForeignKey(Document)
	name=models.CharField(max_length=100, blank=False)
	type=models.CharField(max_length=2, choices=STUDY_DOCUMENT_TYPE, blank=False)
	compulsory=models.CharField(max_length=1, choices=YN, blank=False, default='Y')
	year=models.CharField(max_length=4, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.name
		
		