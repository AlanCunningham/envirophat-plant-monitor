import json
import subprocess
from envirophat import light, weather, analog
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from monitor.models import SensorData


class Command(BaseCommand):

    help = "Gets sensor data from the envirophat and saves to the database"

    def get_calibrated_temperature(self):
        """
        The temperature of the Raspberry Pi CPU can affect the envirophat
        sensor. We try to factor this in using the following formula:
        temp_calibrated = temp_c — ((cpu_temp_c — temp_c)/FACTOR)
        https://medium.com/@InitialState/tutorial-review-enviro-phat-for-raspberry-pi-4cd6d8c63441
        """
        FACTOR = 1.5
        pi_temp_output = subprocess.run(
            ["vcgencmd", "measure_temp"], capture_output=True
        ).stdout
        pi_temp = float(str(pi_temp_output).split("=")[1].split("'")[0])
        env_temp = weather.temperature()
        calibrated_temperature = env_temp - ((pi_temp - env_temp) / FACTOR)
        return int(calibrated_temperature)

    def handle(self, *args, **options):
        """
        Log the temperature, light (normalised) and moisture (normalised) to
        the database.
        """
        light_sensor_max = 1000
        light_sensor_min = 0
        light_normalised = (light.light() - light_sensor_min) / (
            light_sensor_max - light_sensor_min
        )

        moisture_sensor_max = 4.455
        moisture_sensor_min = 0
        moisture_normalised = (analog.read(0) - moisture_sensor_min) / (
            moisture_sensor_max - moisture_sensor_min
        )

        temperature_calibrated = self.get_calibrated_temperature()
        print(f"Light level: {light_normalised} | ({light.light()})")
        print(f"Temperature: {temperature_calibrated}")
        print(f"Soil moisture: {moisture_normalised}")

        sensor_data = SensorData(
            temperature=temperature_calibrated,
            moisture=moisture_normalised,
            light=light_normalised,
        )
        sensor_data.save()
