from django.db import models
from django.utils import timezone
from account.models import CUser
from ckeditor.fields import RichTextField
from filemanager.models import FileStorage
from tag.models import Tag

PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=255, blank=False)
    header=RichTextField(max_length=255,blank=True)
    content=RichTextField(blank=False)
    created_time=models.DateTimeField(default=timezone.now())
    create_by=models.ForeignKey(CUser)
    public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
    attach=models.ManyToManyField(FileStorage, blank=True)
    tag=models.ManyToManyField(Tag, blank=True)
    deactived=models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
    def get_time(self):
        time=self.created_time
        return time
class NewsGuestView(models.Model):
    news=models.ForeignKey(News)
    view_time=models.DateTimeField(default=timezone.now())
class NewsView(models.Model):
    view_time=models.DateTimeField(default=timezone.now())
    news=models.ForeignKey(News)
    user=models.ForeignKey(CUser)