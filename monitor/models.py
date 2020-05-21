from django.db import models
from django.conf import settings
from django.utils.dateformat import format

class SensorData(models.Model):

    datetime = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()
    moisture = models.DecimalField(max_digits=3, decimal_places=2)
    light = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return format(self.datetime, settings.DATETIME_FORMAT)
