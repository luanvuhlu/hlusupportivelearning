from django.db import models
from django.utils import timezone
# from student.models import Student
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    is_public = models.BooleanField(default=True, blank=False)
    created_date = models.DateTimeField(default=timezone.now(), blank=False)
    activated = models.BooleanField(default=True, blank=False)
    description = models.TextField(max_length=200, blank=True)
    def __unicode__(self):
        return self.name
# class StudentTag(models.Model):
#     student=models.ForeignKey(Student)
#     tag=models.ForeignKey(Tag)
#     add_date=models.DateField(default=timezone.now(), blank=False)
#     is_notification=models.BooleanField(default=True, blank=False)
#     is_public=models.BooleanField(default=True, blank=False)
#     activated=models.BooleanField(default=True, blank=False)
