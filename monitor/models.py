from django.db import models


class Reading(models.Models):
    temperature = models.DecimalField()
    moisture = models.DecimalField(decimal_places=2)
    light = models.DecimalField()
