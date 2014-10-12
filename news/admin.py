from django.contrib import admin
from models import News, NewsGuestView, NewsView
class NewsAdmin(admin.ModelAdmin):
    readonly_fields=('create_by', )
    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        obj.save()
    def delete_model(self, request, obj):
        obj.deactived=True
        obj.save()
class NewsGuestViewAdmin(admin.ModelAdmin):
    pass
class NewsViewAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(NewsGuestView, NewsGuestViewAdmin)
admin.site.register(NewsView, NewsViewAdmin)