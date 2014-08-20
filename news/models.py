from django.db import models
from datetime import datetime
from account.models import Manager
from account.models import CUser


# Create your models here.
class News(models.Model):
    title=models.TextField(max_length=255, blank=False)
    header=models.TextField(max_length=255,blank=False)
    content=models.TextField(blank=False)
    created_time=models.DateTimeField(default=datetime.now())
    manager=models.ForeignKey(Manager)
class NewsGuestView(models.Model):
    news=models.ForeignKey(News)
    view_time=models.DateTimeField(default=datetime.now())
class NewsView(models.Model):
    view_time=models.DateTimeField(default=datetime.now())
    news=models.ForeignKey(News)
    user=models.ForeignKey(CUser)