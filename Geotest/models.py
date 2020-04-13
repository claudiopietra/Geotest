from django.contrib import admin
from django.db import models

class Location(models.Model):
    locationname = models.CharField(max_length=255)
    locationidx = models.CharField(max_length=255)
    htmlbody = models.TextField()

    def __str__(self):
        return '{} / {}'.format(self.locationname, self.locationidx)
        
        
class Item(models.Model):
    itemname = models.CharField(max_length=255)
    itemidx = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.itemname)
        
class ItemAdmin(admin.ModelAdmin):
    list_display('itemidx', 'itemname')