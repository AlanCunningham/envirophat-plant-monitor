import json
import subprocess
from envirophat import light, weather, analog
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from monitor.models import SensorData

class Command(BaseCommand):

    help = "Gets sensor data from the envirophat and saves to the database"

    def get_calibrated_temperature():
        """
        The temperature of the Raspberry Pi CPU can affect the envirophat
        sensor. We try to factor this in using the following formula:
        temp_calibrated = temp_c — ((cpu_temp_c — temp_c)/FACTOR)
        https://medium.com/@InitialState/tutorial-review-enviro-phat-for-raspberry-pi-4cd6d8c63441
        """
        FACTOR = 1.5
        pi_temp_output = subprocess.run(["vcgencmd", 'measure_temp'],
            capture_output=True).stdout
        pi_temp = float(str(pi_temp_output).split("=")[1].split("'")[0])
        env_temp = weather.temperature()
        calibrated_temperature = env_temp-((pi_temp-env_temp)/FACTOR)
        return int(calibrated_temperature)

    def handle(self, *args, **options):
        # Convert light level to a percentage
        light_sensor_max = 65535
        light_level = int(light.light() / light_sensor_max * 100)

        # Convert moisture level to a percentage
        moisture_sensor_max = 4.016
        soil_moisture  = int(analog.read(0) / moisture_sensor_max * 100)

        temperature = get_calibrated_temperature()
        timestamp = datetime.now().strftime("%d %b    %H:%M")

        print(f"Date: {timestamp}")
        print(f"Light level: {light_level}")
        print(f"Temperature: {temperature}")
        print(f"Soil moisture: {soil_moisture}")

        sensor_data = {
            'timestamp': timestamp,
            'light_level': light_level,
            'temperature': temperature,
            'soil_moisture': soil_moisture,
        }
