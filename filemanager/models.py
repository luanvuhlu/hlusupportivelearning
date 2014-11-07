from django.db import models
from filebrowser.fields import FileBrowseField
from django.utils import timezone
from account.models import CUser
import hashlib

# Create your models here.
class FileType(models.Model):
	FILE_TYPE_CHOICE={
		("avatar", "avatar"),
		("doc", "doc"),
		("news", "news"),
	}
	name=models.CharField(max_length=20, blank=False)
	extension=models.CharField(max_length=30, blank=False, default="jpg, png")
	description=models.CharField(max_length=200, blank=True)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.name
class FileStorage(models.Model):
	name=models.CharField(max_length=100, blank=False)
	file=FileBrowseField(max_length=200, directory="files/", extensions=[".pdf",".doc", ".docx", 'jpge', 'jpg', 'png'],null=False, blank=False)
	file_type=models.ForeignKey(FileType)
	created_time=models.DateTimeField(default=timezone.now())
	uploader=models.ForeignKey(CUser)
	activated=models.BooleanField(default=True)
	def __unicode__(self):
		return self.file_type.name+"-"+self.name
	def save(self, request=False, *args, **kwargs):
	    if request:
	        self.uploader=request.user
	    super(FileStorage, self).save(*args, **kwargs)
class FileStorageTmp(models.Model):
	code=models.CharField(max_length=10, blank=False)
	name=models.CharField(max_length=100, blank=False)
	uploader=models.ForeignKey(CUser)
	file=FileBrowseField(max_length=200, directory="files_tmp/", extensions=[".pdf",".doc", ".docx", '.jpge', '.jpg', '.png'],null=False, blank=False)
        file_type=models.ForeignKey(FileType)
        created_time=models.DateTimeField(default=timezone.now())
        current_session=models.BooleanField(default=True)
        complete=models.BooleanField(default=False)
        def __unicode__(self):
            return self.file_type.name+"-"+self.name
        def convert(self):
            try:
                obj=FileStorage()
                obj.name=self.name
                obj.file=self.file
                obj.file_type=self.file_type
                obj.uploader=self.uploader
                obj.save()
                self.complete=True
                return obj
            except:
                return None



