from datetime import  timedelta
from django.utils import timezone
from django.db import models
from account.models import CUser
from document.models import Subject
import logging

log=logging.getLogger(__name__)
PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))

GROUP_STATUS_CHOICES=(
    ("F", "FINDING"),
    ("D", "CLOSED"),
)

class Group(models.Model):
    subject=models.ForeignKey(Subject)
    user=models.ForeignKey(CUser, verbose_name="Creater")
    group_leader=models.CharField(max_length=50, blank=True, verbose_name="Group leader name")
    class_theory=models.CharField(max_length=5, blank=False, verbose_name="Theory (N)")
    class_seminar=models.CharField(max_length=5, blank=True, verbose_name="Seminar (TL)")
    date_valid_until=models.DateField(default=(timezone.now()+timedelta(days=7)), blank=False)
    group_name=models.CharField(max_length=5, blank=False)
    status=models.CharField(max_length=2, choices=GROUP_STATUS_CHOICES, default=GROUP_STATUS_CHOICES[0], blank=False)
    phone=models.CharField(max_length=13, blank=False)
    email=models.EmailField(max_length=50, blank=False)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
    created_time=models.DateTimeField(default=timezone.now(), blank=False)
    activated=models.BooleanField(default=True)
    def __unicode__(self):
        return self.subject.__str__()
    def get_date_until(self):
        if not self.date_valid_until:
            return None
        return self.date_valid_until.strftime('%m/%d/%Y')
class GroupMember(models.Model):
    full_name=models.CharField(max_length=50, blank=False)
    member_code=models.CharField(max_length=7, blank=False)
    group=models.ForeignKey(Group)
    add_time=models.DateTimeField(default=timezone.now(), blank=False)
    found_yn=models.BooleanField(default=False, blank=False)
    activated=models.BooleanField(default=True, blank=False)
    def __unicode__(self):
        return self.member_code