from django.contrib import admin
from models import News, NewsGuestView, NewsView

class NewsAdmin(admin.ModelAdmin):
    pass
class NewsGuestViewAdmin(admin.ModelAdmin):
    pass
class NewsViewAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(NewsGuestView, NewsGuestViewAdmin)
admin.site.register(NewsView, NewsViewAdmin)