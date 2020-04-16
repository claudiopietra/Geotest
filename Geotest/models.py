from django.contrib import admin
from django.db import models

class Location(models.Model):
    locationname = models.CharField(max_length=255)
    locationidx = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, default="", blank=True)
    in_inventory = models.CharField(max_length=255, default="", blank=True)
    not_in_inventory = models.CharField(max_length=255, default="", blank=True)
    htmlbody = models.TextField()

    def __str__(self):
        return self.locationname
        
        
class Item(models.Model):
    itemname = models.CharField(max_length=255)
    itemidx = models.CharField(max_length=255)
    htmlbody_add = models.TextField()
    htmlbody_remove = models.TextField()
    
    def __str__(self):
        return self.itemname
