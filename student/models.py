from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from tag.models import Tag
from account.models import CUser
import logging
log=logging.getLogger(__name__)
# Create your models here.
PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
class Scholastic(models.Model):
    name=models.CharField(max_length=20, blank=True, unique=True)
    start_date=models.DateField(blank=False)
    end_date=models.DateField(blank=False)
    description=models.TextField(max_length=200, blank=True)
    public=models.BooleanField(default=True)
    activated=models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
class Course(models.Model):
    code=models.CharField(max_length=10, blank=False, unique=True)
    name=models.CharField(max_length=32, blank=True)
    scholastic_start=models.ForeignKey(Scholastic)
    activated=models.BooleanField(default=True)
    public=models.BooleanField(default=True)
    description=models.TextField(max_length=200, blank=True)
    def __unicode__(self):
        return self.code

class UClass(models.Model):
    code=models.CharField(max_length=5, unique=True, blank=False)
    name=models.CharField(max_length=10, blank=True)
    course=models.ForeignKey(Course)
    activated=models.BooleanField(default=True)
    public=models.BooleanField(default=True)
    description=models.TextField(max_length=200, blank=True)
    def __unicode__(self):
        return self.code
class Student(models.Model):
    account=models.OneToOneField(CUser)
    u_class=models.ForeignKey(UClass)
    first_name=models.CharField(max_length=100, blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    alias=models.CharField(max_length=100, blank=True)
    email=models.EmailField(blank=True)
    mobile_phone=models.CharField(max_length=20, blank=True)
    telephone=models.CharField(max_length=20, blank=True)
    code=models.CharField(max_length=7, blank=False, unique=True)
    birthday=models.DateField(blank=False)
    block=models.BooleanField(default=False)
    activated=models.BooleanField(default=True)
    tags=models.ManyToManyField(Tag, blank=True)
    def __unicode__(self):
        return self.code
    def clean(self):
        if self.code and len(self.code) < 6:
            log.debug('Code is invalid')
            raise ValidationError('Code is invalid.')
        try:
            st=Student.objects.filter(code=self.code)
            if st:
                raise ValidationError('Code is already exist.')
        except Exception as e:
            log.debug(e.message.__str__())
    def save(self, request=False, *args, **kwargs):
        if request:
            self.account=request.user
        super(Student, self).save(*args, **kwargs)



