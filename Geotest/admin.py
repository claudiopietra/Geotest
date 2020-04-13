from django.contrib import admin
from .models import Location
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemname', 'itemidx')

admin.site.register(Item, ItemAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationname', 'locationidx', 'comment', 'in_inventory', 'not_in_inventory')

admin.site.register(Location, LocationAdmin)
