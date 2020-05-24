from django.core.management.base import BaseCommand
from monitor.models import SensorData
from ... import sensor_helper


class Command(BaseCommand):

    help = "Gets sensor data from the envirophat and saves to the database"


    def handle(self, *args, **options):
        """
        Log the temperature, light (normalised) and moisture (normalised) to
        the database.
        """
        sensor_reading = sensor_helper.get_sensor_data()
        sensor_data = SensorData(
            temperature=sensor_reading["temperature"],
            moisture=sensor_reading["moisture"],
            light=sensor_reading["light"],
        )
        sensor_data.save()
