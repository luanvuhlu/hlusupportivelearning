from datetime import  timedelta, datetime
from django.utils import timezone
from django.db import models
from account.models import CUser
from studentinfo.models import Student
from document.models import Subject

PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
FINDING_GROUP_TYPE_CHOICES=(
        ("S", "Self"),
        ("H", "Help"),
    )
FINDING_GROUP_STATUS_CHOICES=(
    ("F", "FINDING"),
    ("D", "DONE"),
)
# Create your models here.
# class Subject(models.Model):
#     subject_code=models.CharField(max_length=20, blank=False)
#     subject_name=models.CharField(max_length=100,blank=False)
#     subject_short_name=models.CharField(max_length=30, blank=True)
#     def __unicode__(self):
#         if self.subject_short_name:
#             return self.subject_short_name
#         return self.subject_code
class FindingGroupNews(models.Model):
    subject=models.ForeignKey(Subject)
    user=models.ForeignKey(CUser, verbose_name="Creater")
    finding_group_type=models.CharField(max_length=2, choices=FINDING_GROUP_TYPE_CHOICES, default=FINDING_GROUP_TYPE_CHOICES[0])
    group_leader=models.CharField(max_length=50, blank=True, verbose_name="Group leader name")
    class_theory=models.CharField(max_length=5, blank=False, verbose_name="Theory (N)")
    class_seminar=models.CharField(max_length=5, blank=True, verbose_name="Seminar (TL)")
    date_valid_until=models.DateTimeField(default=(timezone.now()+timedelta(days=7)), blank=False)
    status=models.CharField(max_length=2, choices=FINDING_GROUP_STATUS_CHOICES, default=FINDING_GROUP_STATUS_CHOICES[0])
    phone=models.CharField(max_length=13, blank=False)
    email=models.EmailField(max_length=50, blank=False)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
    date_created=models.DateTimeField(default=timezone.now(), blank=False)
    deactived=models.BooleanField(default=False)
    def __unicode__(self):
        return self.subject.__str__()
    @staticmethod
    def create_group(subject_code, theory, seminar, date_valid, leader_name, phone, email, user):
        gr=FindingGroupNews()
        try:
            subject=Subject.objects.get(deactived=False, public='Y', subject_code=subject_code)
        except Subject.DoesNotExist:
            return None
        gr.subject=subject
        gr.user=user
        gr.class_theory=theory
        gr.class_seminar=seminar
        date_obj=datetime.strptime(date_valid, '%m/%d/%Y')
        gr.date_valid_until=date_obj
        gr.group_leader=leader_name
        gr.phone=phone
        gr.email=email
        return gr
class GroupMemberUnknown(models.Model):
    full_name=models.CharField(max_length=50, blank=False)
    member_student_code=models.CharField(max_length=7, blank=False)
    finding_group=models.ForeignKey(FindingGroupNews)
    def __unicode__(self):
        return self.full_name
class GroupMember(models.Model):
    student=models.ForeignKey(Student)
    finding_group=models.ForeignKey(FindingGroupNews)
    add_time=models.DateTimeField(default=timezone.now(), blank=False)
    deactived=models.BooleanField(default=False)
    def __unicode__(self):
        return self.student.student_code