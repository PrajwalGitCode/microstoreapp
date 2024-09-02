from django.contrib import admin
from .models import Watches, Laptop, Mobile, Graphic,Processor,Accessory
from .models import WatchesUploads
# Register your models here.


class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',"image")
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    fields = ['name', 'description', 'price', 'image']

admin.site.register(Watches)
admin.site.register(Laptop)
admin.site.register(Mobile)
admin.site.register(Graphic)
admin.site.register(Processor)
admin.site.register(Accessory)
admin.site.register(WatchesUploads, WatchesUploadsAdmin)
