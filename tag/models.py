from django.db import models
from django.utils import timezone
# Create your models here.
PUBLIC_YN=(('Y', 'Y'), ('N', 'N'))
YN=(('Y', 'Y'), ('N', 'N'))
class Tag(models.Model):
	name=models.CharField(max_length=100, blank=False)
	public=models.CharField(max_length=1, choices=PUBLIC_YN, default='Y')
	count=models.IntegerField(default=0)	
	created_time=models.DateTimeField(default=timezone.now(), blank=False)
	deactived=models.BooleanField(default=False)