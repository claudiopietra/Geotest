from django.contrib import admin
from django.db import models

# a location in the adventure
class Location(models.Model):
    locationname = models.CharField(max_length=255)
    locationidx = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, default="", blank=True)
    in_inventory = models.CharField(max_length=255, default="", blank=True)
    not_in_inventory = models.CharField(max_length=255, default="", blank=True)
    was_in_inventory = models.CharField(max_length=255, default="", blank=True)
    default = models.BooleanField(default=False)
    htmlbody = models.TextField(blank=True)

    def __str__(self):
        return self.locationname


#an item in the adventure
class Item(models.Model):
    itemname = models.CharField(max_length=255)
    itemidx = models.CharField(max_length=255)
    htmlbody_add = models.TextField(blank=True)
    htmlbody_remove = models.TextField(blank=True)

    def __str__(self):
        return self.itemname
