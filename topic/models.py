from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from account.models import CUser


PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
# Create your models here.
class Topic(models.Model):
    title=models.TextField(max_length=255, blank=False)
    header=RichTextField(max_length=255, blank=True)
    content=RichTextField(blank=False)
    created_time=models.DateTimeField(default=datetime.now(), blank=False)
    user=models.ForeignKey(CUser)
    deactived=models.BooleanField(default=False)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
class TopicView(models.Model):
    view_time=models.DateTimeField(default=datetime.now(), blank=False)
    user=models.ForeignKey(CUser)
    topic=models.ForeignKey(Topic)
class TopicGuestView(models.Model):
    view_time=models.DateTimeField(default=datetime.now(), blank=False)
    topic=models.ForeignKey(Topic)
class TopicThanks(models.Model):
    thank_time=models.DateTimeField(default=datetime.now(), blank=False)
    user=models.ForeignKey(CUser)
    topic=models.ForeignKey(Topic)
class Comment(models.Model):
    content=models.TextField(max_length=255, blank=False)
    comment_time=models.DateTimeField(default=datetime.now(), blank=False)
    topic=models.ForeignKey(Topic)
    user=models.ForeignKey(CUser)
    deactived=models.BooleanField(default=False)