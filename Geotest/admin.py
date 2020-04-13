from django.contrib import admin
from .models import Location
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemidx', 'itemname')


admin.site.register(Location)
admin.site.register(Item, ItemAdmin)