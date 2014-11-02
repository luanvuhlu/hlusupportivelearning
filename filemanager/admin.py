from django.contrib import admin
from models import FileStorage, FileType, FileStorageTmp
class FileTypeAdmin(admin.ModelAdmin):
	eadonly_fields = ('activated', )
	exclude = ('user', )
	def save_model(self, request, obj, form, change):
		obj.save()
	def delete_model(self, request, obj):
		obj.activated=False
		obj.save()
class FileStorageAdmin(admin.ModelAdmin):
	eadonly_fields = ('activated', )
	exclude = ('user', )
	def save_model(self, request, obj, form, change):
		obj.save(request)
	def delete_model(self, request, obj):
		obj.activated=False
		obj.save()
class FileStorageTmpAdmin(admin.ModelAdmin):
	eadonly_fields = ('activated', )
	exclude = ('user', )
	def save_model(self, request, obj, form, change):
		obj.uploader=request.user
		obj.save(request)
	def delete_model(self, request, obj):
		obj.activated=False
		obj.save()
# Register your models here.
admin.site.register(FileType, FileTypeAdmin)
admin.site.register(FileStorage, FileStorageAdmin)
admin.site.register(FileStorageTmp, FileStorageTmpAdmin)