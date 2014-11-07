from django.db import models
from django.utils import timezone
from account.models import CUser
# Create your models here.

class Holiday(models.Model):
    TIME_OF_DAY_CHOICES=((0, "Day"), (1, "Morning"), (2, 'Afternoon'))
    name=models.CharField(max_length=200, blank=True)
    date=models.DateField(blank=False)
    time_of_day=models.SmallIntegerField(choices=TIME_OF_DAY_CHOICES, default=0)
    created_time=models.DateTimeField(default=timezone.now())
    user=models.ForeignKey(CUser)
    desciption=models.CharField(max_length=200, blank=True)
    public=models.BooleanField(default=True)
    activated=models.BooleanField(default=True)
    def __unicode__(self):
        return self.name