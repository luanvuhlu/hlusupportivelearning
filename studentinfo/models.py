from django.db import models
from account.models import CUser

# Create your models here.

class Course(models.Model):
    course_code=models.CharField(max_length=10, blank=False, unique=True)
    course_name=models.CharField(max_length=32, blank=False)
    def __unicode__(self):
        return self.course_code
class Speciality(models.Model):
    speciality_code=models.CharField(max_length=5, blank=False, unique=True)
    speciality_name=models.CharField(max_length=50, blank=False)
    def __unicode__(self):
        return self.speciality_code
class UClass(models.Model):
    class_code=models.CharField(max_length=5, blank=False)
    class_name=models.CharField(max_length=10, blank=False)
    course=models.ForeignKey(Course)
    speciality=models.ForeignKey(Speciality)
    def __unicode__(self):
        return self.class_code
class Student(models.Model):
    uclass=models.ForeignKey(UClass)
    course=models.ForeignKey(Course)
    speciality=models.ForeignKey(Speciality)
    student_code=models.CharField(max_length=7, blank=False, unique=True)
    facebook_link=models.URLField(max_length=100, blank=True)
    user=models.ForeignKey(CUser)
    def __unicode__(self):
        return self.student_code