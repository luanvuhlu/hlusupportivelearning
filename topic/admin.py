from django.contrib import admin
from models import Topic, TopicView, TopicGuestView, Comment
# Register your models here.
admin.site.register(Topic)
admin.site.register(TopicView)
admin.site.register(TopicGuestView)
admin.site.register(Comment)