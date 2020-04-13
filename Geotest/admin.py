from django.contrib import admin
from .models import Location
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemname', 'itemidx')

admin.site.register(Item, ItemAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationname', 'locationidx')

admin.site.register(Location, LocationAdmin)
