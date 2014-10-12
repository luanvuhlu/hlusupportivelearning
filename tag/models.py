from django.db import models
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    is_public = models.BooleanField(default=True, blank=False)
    created_date = models.DateTimeField(default=timezone.now(), blank=False)
    activated = models.BooleanField(default=True)
    description = models.TextField(max_length=200, blank=True)