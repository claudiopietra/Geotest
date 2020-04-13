from django.db import models

class Location(models.Model):
    locationname = models.CharField(max_length=255)
    locationidx = models.CharField(max_length=255)
    htmlbody = models.TextField()

    def __str__(self):
        return '{} / {}'.format(self.locationname, self.locationidx)