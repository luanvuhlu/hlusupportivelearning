from django.contrib import admin
from models import News, NewsGuestView, NewsView
from account.models import Manager

class NewsAdmin(admin.ModelAdmin):
    readonly_fields=('manager', )
    def save_model(self, request, obj, form, change):
        try:
            manager=Manager.objects.get(user=request.user)
        except Manager.DoesNotExist:
            manager=None

        obj.manager = manager

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