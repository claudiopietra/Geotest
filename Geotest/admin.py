from django.contrib import admin
from .models import Location
from .models import Item

admin.site.register(Location)
admin.site.register(Item)