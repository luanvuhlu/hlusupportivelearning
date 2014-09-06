from django.db import models
from filebrowser.fields import FileBrowseField
from django.utils import timezone

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
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return self.name
class FileStorage(models.Model):
	name=models.CharField(max_length=100, blank=False)
	file=FileBrowseField("DOC",max_length=200, directory="files/", extensions=[".pdf",".doc", ".docx"],null=False, blank=False)
	file_type=models.ForeignKey(FileType)
	created_time=models.DateTimeField(default=timezone.now())
	deactived=models.BooleanField(default=False)
	def __unicode__(self):
		return self.file_type.name+"-"+self.name

