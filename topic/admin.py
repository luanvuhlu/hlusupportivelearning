from django.contrib import admin
from models import Topic, TopicView, TopicGuestView, Comment

class TopicAdmin(admin.ModelAdmin):
	list_display  = ('title', 'created_time', 'user', 'public', 'block', 'activated')
	readonly_fields = ('activated', 'created_time', 'edited' )
	date_hierarchy = 'created_time'
	exclude = ('user', )
	list_filter = ( 'created_time', 'user__username', 'public', 'block', 'activated', 'edited')
	search_fields = ['title', 'content']
	def save_model(self, request, obj, form, change):
	    obj.user=request.user
	    obj.save()
	def delete_model(self, request, obj):
	    obj.activated=False
	    obj.save()
# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicView)
admin.site.register(TopicGuestView)
admin.site.register(Comment)