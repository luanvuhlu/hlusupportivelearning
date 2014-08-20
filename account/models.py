#!/usr/bin/env python
#coding: utf8
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class CUser(AbstractUser):
    GENDER_CHOOICE=(
        (True, "Male"),
        (False, "Female"),
    )
    PROVINCE_CODE_CHOOICE=(
        (0, "Choose one"),
        (1, "Hà Nội"),
    )
    alias=models.CharField(max_length=50, blank=True)
    password_reset_link=models.URLField(max_length=100, blank=True)
    password_reset_until=models.DateTimeField(blank=False, default=datetime.now())
    phone=models.CharField(max_length=13, blank=True)
    address=models.TextField(max_length=100, blank=True)
    province_code=models.SmallIntegerField(default=0, choices=PROVINCE_CODE_CHOOICE)
    gender=models.BooleanField(default=True, choices=GENDER_CHOOICE)
    introduce=models.TextField(max_length=200, blank=True)
    def __unicode__(self):
        if self.alias:
            return self.alias
        return self.username
class Manager(models.Model):
    user=models.ForeignKey(CUser)
    def __unicode__(self):
        return self.user.__str__()
