from django.db import models


class SensorData(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    temperature = models.IntegerField()
    moisture = models.DecimalField(max_digits=2, decimal_places=2)
    light = models.DecimalField(max_digits=2, decimal_places=2)
