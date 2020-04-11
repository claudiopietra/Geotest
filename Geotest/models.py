from django.db import models

class Ort(models.Model):
    ortname = models.CharField(max_length=255)
    ortidx = models.CharField(max_length=255)
    htmlbody = models.TextField()

    def __str__(self):
        return '{} / {}'.format(self.ortname, self.ortidx)