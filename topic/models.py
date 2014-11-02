from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from account.models import CUser
from filemanager.models import FileStorage
from tag.models import Tag
import logging

log=logging.getLogger(__name__)
# Create your models here.
class Topic(models.Model):
    title=models.CharField(max_length=255, blank=False)
    header=RichTextField(max_length=255, blank=True)
    content=RichTextField(blank=False)
    created_time=models.DateTimeField(default=datetime.now(), blank=False)
    user=models.ForeignKey(CUser)
    attach=models.ManyToManyField(FileStorage, blank=True)
    tag=models.ManyToManyField(Tag, blank=True)
    activated=models.BooleanField(default=True)
    public=models.BooleanField(default=True)
    block=models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
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
    block=models.BooleanField(default=False)
    edited=models.BooleanField(default=False)
    activated=models.BooleanField(default=True)
