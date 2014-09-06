from django.contrib import admin
from models import FileStorage, ImageStorage, FileType
# Register your models here.
admin.site.register(FileType)
admin.site.register(FileStorage)
admin.site.register(ImageStorage)